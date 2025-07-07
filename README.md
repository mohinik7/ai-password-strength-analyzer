# AI Password Strength Analyzer

A modern web application that analyzes password strength using both heuristic rules and a machine learning model. It provides instant feedback on password quality, helping users create stronger, more secure passwords.

---

## Features

- **Heuristic Analysis:** Rule-based scoring for length, character variety, and more.
- **AI/ML Prediction:** Neural network model trained on a large, labeled password dataset.
- **Advanced Normalization:** Handles leet-speak and repeated characters.
- **Hybrid Override:** Ensures truly strong passwords are always recognized.


---

## Tech Stack

- **Frontend:** React.js (JavaScript)
- **Backend:** Python Flask
- **Machine Learning:** scikit-learn (MLPClassifier), StandardScaler
- **Data Processing:** pandas, numpy
- **Other:** NLTK (for optional semantic analysis), joblib

---


## Getting Started

### 1. Clone the repository

```sh
git clone https://github.com/yourusername/ai-password-strength-analyzer.git
cd ai-password-strength-analyzer
```

### 2. Backend Setup

```sh
cd backend
pip install -r requirements.txt
python app.py
```

The backend will run at `http://localhost:5000`

### 3. Frontend Setup

```sh
cd frontend
npm install
npm start
```

The frontend will run at `http://localhost:3000`

---

##  Usage

- Open [http://localhost:3000](http://localhost:3000) in your browser.
- Enter a password to analyze its strength.
- View the normalized password, heuristic score, and ML prediction.

---

## Model Details

- **ML Model:** MLPClassifier (Neural Network) trained on a labeled dataset with 5 strength levels (0=Very Weak, 1= Weak, 2= Medium, 3= Strong, 4=Very Strong).
- **Features Used:** Length, capital/small/special/numeric counts, entropy, sequence detection, character diversity, character type distribution.
- **Hybrid Override:** Ensures long, random, high-entropy passwords are always rated as "Very Strong."

---

