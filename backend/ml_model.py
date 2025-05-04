import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv('dataset/passwords.csv')

def preprocess(pw):
    return re.sub(r'[^a-zA-Z0-9]', '', pw.lower())

data['password'] = data['password'].apply(preprocess)
X = data['password']
y = data['strength']

vectorizer = CountVectorizer(analyzer='char', ngram_range=(2, 3))
X_vec = vectorizer.fit_transform(X)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_vec, y)

joblib.dump(model, 'dataset/model.pkl')
joblib.dump(vectorizer, 'dataset/vectorizer.pkl')

model = joblib.load('dataset/model.pkl')
vectorizer = joblib.load('dataset/vectorizer.pkl')

def predict_strength(password):
    pw = preprocess(password)
    vec = vectorizer.transform([pw])
    return int(model.predict(vec)[0])
