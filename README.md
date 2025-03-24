# 📊 News Sentiment Analysis

A **web-based sentiment analysis application** that fetches recent news about a company, analyzes sentiment, and provides results in **text and Hindi audio**.

## 🚀 Features
- 🔍 Fetches news articles from NewsAPI
- 🎯 Filters relevant company-related articles
- 📊 Performs sentiment analysis using **NLTK (VADER)**
- 📌 Displays sentiment distribution
- 🌐 Web-based UI with **Streamlit**
- ⚡ REST API using **FastAPI**
- 🔊 Generates Hindi speech output with **gTTS**

## 📂 Project Structure
```
📁 news-sentiment-analysis/
│── app.py              # Streamlit Web App
│── api.py              # FastAPI Backend
│── utils.py            # Helper Functions
│── requirements.txt    # Dependencies with Versions
│── README.md           # Documentation
```

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/news-sentiment-analysis.git
cd news-sentiment-analysis
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Web App (Streamlit)
```sh
streamlit run app.py
```

### 4️⃣ Run the REST API (FastAPI)
```sh
uvicorn api:app --reload
```
**API Endpoint:** `http://127.0.0.1:8000/analyze?company=Google`

## 🚀 Deployment
### Deploy on Hugging Face Spaces:
1. Upload `app.py`, `api.py`, `utils.py`, and `requirements.txt`.
2. Set up **Hugging Face Spaces** for Streamlit.
3. Your app will be live at `https://huggingface.co/spaces/Sreek7170/News.summarization`.

## 🤝 Contributing
Pull requests are welcome! Feel free to open an issue for bug fixes or enhancements.

## 🛠 Technologies Used
- **Python 3.10+**
- **Streamlit** (Web UI)
- **FastAPI** (API Backend)
- **NLTK (VADER)** (Sentiment Analysis)
- **Requests** (Fetching News)
- **gTTS** (Text-to-Speech)

## 📜 License
This project is licensed under the MIT License.

🚀 **Happy Coding!**
