import requests
import json
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from gtts import gTTS
import os

# Download the VADER lexicon once
nltk.download('vader_lexicon', quiet=True)

API_KEY = "062facad445942afbc769462d3e7d690"  # Replace with your actual NewsAPI key

def fetch_articles(company, fetch_count=30):
    url = f"https://newsapi.org/v2/everything?q={company}&pageSize={fetch_count}&apiKey={API_KEY}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error fetching news:", response.text)
        return []
    
    data = response.json()
    return [
        {
            "title": item.get("title", "No Title"),
            "summary": item.get("description") or "No Summary",
            "publishedAt": item.get("publishedAt", "")
        }
        for item in data.get("articles", [])
    ]

def filter_articles_by_relevance(articles, company):
    company_lower = company.lower()
    return [
        article for article in articles
        if company_lower in article.get("title", "").lower() or
           company_lower in article.get("summary", "").lower()
    ]

def analyze_sentiment(articles):
    sia = SentimentIntensityAnalyzer()
    for article in articles:
        score = sia.polarity_scores(article.get("summary", ""))
        article["sentiment"] = "Positive" if score["compound"] > 0.05 else "Negative" if score["compound"] < -0.05 else "Neutral"
        article["sentiment_score"] = score["compound"]
    return articles

def comparative_sentiment_analysis(articles):
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    for article in articles:
        sentiment_counts[article.get("sentiment", "Neutral")] += 1
    return sentiment_counts

def finalize_sentiment_analysis_in_hindi(sentiment_counts):
    if sentiment_counts["Positive"] > sentiment_counts["Negative"]:
        return "कुल मिलाकर, समाचार कवरेज सकारात्मक है।"
    elif sentiment_counts["Negative"] > sentiment_counts["Positive"]:
        return "कुल मिलाकर, समाचार कवरेज नकारात्मक है।"
    else:
        return "कुल मिलाकर, समाचार कवरेज संतुलित है।"

def text_to_speech_final_sentiment(text, language='hi'):
    tts = gTTS(text=text, lang=language)
    tts.save("final_sentiment.mp3")
