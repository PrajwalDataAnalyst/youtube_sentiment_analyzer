import streamlit as st
import pandas as pd
from youtube_fetcher import get_youtube_comments
from sentiment_analyzer import classify_sentiment

# App title
st.set_page_config(page_title="YouTube Sentiment Analyzer", layout="wide")
st.title("🎬 YouTube Comment Sentiment Analyzer")

# Input
video_url = st.text_input("🔗 Enter YouTube Video URL (e.g. https://www.youtube.com/watch?v=VIDEO_ID):")

if video_url:
    try:
        # Extract video ID
        video_id = video_url.split("v=")[-1].split("&")[0]

        with st.spinner("Fetching comments..."):
            comments = get_youtube_comments(video_id, max_comments=100)

        st.success(f"✅ Fetched {len(comments)} comments.")

        # Analyze sentiment
        results = []
        for comment in comments:
            sentiment = classify_sentiment(comment)
            results.append({'Comment': comment, 'Sentiment': sentiment})

        df = pd.DataFrame(results)

        # Display results
        st.subheader("📊 Sentiment Breakdown")
        sentiment_counts = df['Sentiment'].value_counts()
        st.bar_chart(sentiment_counts)

        st.subheader("🗂️ Detailed Comments")
        st.dataframe(df, use_container_width=True)

        # Download
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Results", csv, "sentiments.csv", "text/csv")

    except Exception as e:
        st.error(f"⚠️ Error: {e}")
