from fastapi import FastAPI
from utils import fetch_articles, filter_articles_by_relevance, analyze_sentiment, comparative_sentiment_analysis, finalize_sentiment_analysis_in_hindi

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the News Sentiment Analysis API"}

@app.get("/analyze/")
def analyze_news(company: str):
    articles = fetch_articles(company)
    if not articles:
        return {"error": "No articles found"}
    
    relevant_articles = filter_articles_by_relevance(articles, company)[:10]
    analyzed_articles = analyze_sentiment(relevant_articles)
    sentiment_counts = comparative_sentiment_analysis(analyzed_articles)
    final_hindi = finalize_sentiment_analysis_in_hindi(sentiment_counts)

    return {
        "Company": company,
        "Sentiment Distribution": sentiment_counts,
        "Overall Sentiment in Hindi": final_hindi,
        "Articles": analyzed_articles
    }
