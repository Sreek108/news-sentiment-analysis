import streamlit as st
from utils import fetch_articles, filter_articles_by_relevance, analyze_sentiment, comparative_sentiment_analysis, finalize_sentiment_analysis_in_hindi, text_to_speech_final_sentiment

st.title("📊 News Sentiment Analyzer")

company_name = st.text_input("Enter a company name:")

if st.button("Analyze News Sentiment"):
    if not company_name:
        st.error("Please enter a company name")
    else:
        st.spinner("Fetching and analyzing news articles...")

        articles = fetch_articles(company_name)
        if not articles:
            st.warning("No articles found.")
        else:
            relevant_articles = filter_articles_by_relevance(articles, company_name)[:10]
            analyzed_articles = analyze_sentiment(relevant_articles)
            sentiment_counts = comparative_sentiment_analysis(analyzed_articles)
            final_hindi = finalize_sentiment_analysis_in_hindi(sentiment_counts)

            st.subheader("Sentiment Analysis")
            st.json(sentiment_counts)
            st.write("📢 **Overall Sentiment in Hindi:**", final_hindi)

            text_to_speech_final_sentiment(final_hindi)
            audio_file = open("final_sentiment.mp3", "rb")
            st.audio(audio_file.read(), format="audio/mp3")
