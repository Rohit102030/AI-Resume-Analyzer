# AI-Resume-Analyzer
# 🚀 AI Resume Analyzer with Chatbot

An intelligent web application that analyzes resumes using **AI, NLP, and Machine Learning**, and provides **job predictions, resume scoring, suggestions, and an AI-powered chatbot assistant**.

---

## 📌 Features

* 📄 Resume Parsing (PDF upload)
* 🧠 AI-based Job Role Prediction
* 💼 Rule-based Job Recommendation
* 📊 Resume Scoring System
* 🧠 Skill Detection (Python, SQL, ML, etc.)
* 🤖 AI Career Chatbot (API-based)
* 🎨 Modern UI with animations (Streamlit)

---

## 🛠️ Tech Stack

* **Frontend/UI:** Python (Streamlit)
* **Backend Logic:** Python
* **Machine Learning:** Scikit-learn
* **NLP:** spaCy
* **PDF Parsing:** PyPDF2
* **AI Chatbot API:** Google Gemini API
* **Deployment:** Streamlit Cloud

---

## ⚙️ Project Structure

```
resume-analyzer/
│── app.py
│── parser.py
│── nlp.py
│── model.py
│── recommender.py
│── dataset.csv
│── requirements.txt
```

---

## 🚀 How It Works

1. User uploads resume (PDF)
2. Text is extracted using PyPDF2
3. NLP preprocessing is applied
4. ML model predicts job role
5. Rule-based system suggests job
6. Resume score is calculated
7. Chatbot provides career guidance

---

## 🧠 Key Concepts Used

* Natural Language Processing (NLP)
* TF-IDF Vectorization
* Naive Bayes Classification
* Text Cleaning & Tokenization
* AI Chatbot Integration

---

## 📥 Installation

### 1. Clone Repository

```
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Install spaCy Model

```
python -m spacy download en_core_web_sm
```

### 4. Run Application

```
streamlit run app.py
```

---

## 🔑 API Setup (Chatbot)

1. Get API key from Google AI Studio
2. Create file:

```
.streamlit/secrets.toml
```

3. Add:

```
GEMINI_API_KEY = "your_api_key_here"
```

---

## 🌐 Deployment

Deployed using **Streamlit Community Cloud**

Steps:

* Push code to GitHub
* Connect repo to Streamlit Cloud
* Deploy app

---

## 📊 Future Improvements

* 🔐 User authentication system
* 📈 Advanced analytics dashboard
* 🤖 More intelligent chatbot (memory-based)
* 🌐 Full-stack version (React + Flask)

---

## ⚠️ Limitations

* Depends on dataset quality
* Chatbot requires internet/API
* Limited accuracy for complex resumes

---

## 👨‍💻 Author

**Rohit Kumar**
B.Tech IT Student

---

