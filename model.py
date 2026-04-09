import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
data = pd.read_csv("dataset.csv")

texts = data["text"]
labels = data["label"]

# Convert text to vectors
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Train model
model = MultinomialNB()
model.fit(X, labels)

def predict_job(text):
    vec = vectorizer.transform([text])
    return model.predict(vec)[0]