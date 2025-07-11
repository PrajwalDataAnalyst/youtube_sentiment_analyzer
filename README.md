
<img align="right" width="300" src="https://media.tenor.com/rePDfDWO3XoAAAAd/hacking.gif" />

# 🎬 YouTube Comment Sentiment Analyzer

A **Streamlit NLP app** that fetches comments from YouTube videos and performs real-time **sentiment analysis** using the **VADER (Valence Aware Dictionary)** — a pre-trained lexicon-based model from `nltk`. No training required!

---

## 🚀 Features

- 🔍 Extract comments using **YouTube Data API**
- 🧠 Analyze sentiment using **VADER sentiment analyzer**
- 📊 View visual breakdown (Positive, Negative, Neutral)
- 📁 Export results to CSV
- ⚡ Fast, lightweight & deployable with Streamlit

---

## 🗂️ Project Structure

```
youtube_sentiment_analyzer/
├── app.py                  # Streamlit app UI logic
├── youtube_fetcher.py      # Fetch comments via YouTube API
├── sentiment_analyzer.py   # NLP sentiment logic using VADER
├── image/
│   └── Screenshot_2025-07-11_134125.png  # Output sample
├── .env                    # API key for YouTube
├── requirements.txt        # Python dependencies
└── README.md               # Project overview and usage
```

---

## 🧠 Tech Stack

- Python, Pandas
- **NLTK (VADER Sentiment Analyzer)**
- Streamlit (for Web App UI)
- YouTube Data API v3
- Matplotlib, Seaborn (for visualization)

---

## 📸 Output Preview

<p align="center">
  <img src="image/Screenshot%202025-07-11%20134125.png" width="80%" alt="Sentiment Analysis Output"/>
</p>

> _Above: Screenshot of the app showing sentiment results with comment table and bar chart._

---

## 🔧 Setup Instructions

1. **Clone the Repo**
```bash
git clone https://github.com/PrajwalDataAnalyst/youtube_sentiment_analyzer.git
cd youtube_sentiment_analyzer
```

2. **Install Requirements**
```bash
pip install -r requirements.txt
```

3. **Set Up API Key**
```env
# Inside .env
YOUTUBE_API_KEY=your_api_key_here
```

4. **Run the App**
```bash
streamlit run app.py
```

---

## 📊 Sample Output Table

| Comment                            | Sentiment |
|------------------------------------|-----------|
| This video is amazing!             | Positive  |
| I didn’t find this useful          | Negative  |
| Could be better, but decent effort | Neutral   |

---

## 🚀 Future Improvements

- Add custom ML/BERT model for deep sentiment
- Clean spam & repetitive comments
- Add topic modeling or keyword extraction
- Deploy to Hugging Face Spaces / Streamlit Cloud

---

## 📜 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for more information.

---

## 🙋‍♂️ Author

- **👤 Name**: Prajwal  
- **🌐 GitHub**: [@PrajwalDataAnalyst](https://github.com/PrajwalDataAnalyst)  
- **✉️ Email**: prajwalint1027@gmail.com

---
