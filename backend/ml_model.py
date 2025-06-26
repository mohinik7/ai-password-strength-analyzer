import re
import joblib
import os
import numpy as np
from sklearn.preprocessing import StandardScaler
import math
from collections import Counter

# Get the directory where ml_model.py is located
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'dataset', 'model_enhanced.pkl')
scaler_path = os.path.join(current_dir, 'dataset', 'scaler_enhanced.pkl')

def extract_features(password):
    # Length
    length = len(password)
    # Capital letters
    capital = sum(1 for c in password if c.isupper())
    # Small letters
    small = sum(1 for c in password if c.islower())
    # Special characters (non-alphanumeric)
    special = len(password) - len(re.findall(r'[\w]', password))
    # Numeric
    numeric = sum(1 for c in password if c.isdigit())
    # Entropy (Shannon)
    if not password:
        entropy = 0
    else:
        counts = Counter(password)
        frequencies = [count / len(password) for count in counts.values()]
        entropy = -sum(freq * math.log2(freq) for freq in frequencies)
    # Sequence detection (increasing only, length 3)
    def has_sequential_chars(pw, length=3):
        for i in range(len(pw) - length + 1):
            seq = pw[i:i+length]
            if seq.isalpha() and seq.islower():
                if ''.join(chr(ord(seq[0]) + j) for j in range(length)) == seq:
                    return 1
            if seq.isalpha() and seq.isupper():
                if ''.join(chr(ord(seq[0]) + j) for j in range(length)) == seq:
                    return 1
            if seq.isdigit():
                if ''.join(str(int(seq[0]) + j) for j in range(length)) == seq:
                    return 1
        return 0
    has_sequence = has_sequential_chars(password)
    # Character diversity (unique/length)
    char_diversity = len(set(password)) / length if length > 0 else 0
    # Character type distribution (stddev of proportions, then normalized)
    def char_type_distribution(pw):
        if not pw:
            return 0
        char_types = [
            sum(c.islower() for c in pw) / len(pw) if any(c.islower() for c in pw) else 0,
            sum(c.isupper() for c in pw) / len(pw) if any(c.isupper() for c in pw) else 0,
            sum(c.isdigit() for c in pw) / len(pw) if any(c.isdigit() for c in pw) else 0,
            sum(not c.isalnum() for c in pw) / len(pw) if any(not c.isalnum() for c in pw) else 0
        ]
        char_types = [ct for ct in char_types if ct > 0]
        if len(char_types) <= 1:
            return 0
        std_dev = np.std(char_types)
        return 1 / (1 + std_dev)
    char_distribution = char_type_distribution(password)
    return [length, capital, small, special, numeric, entropy, has_sequence, char_diversity, char_distribution]

def load_model_with_fallback():
    try:
        # Try loading with the current environment
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        return model, scaler
    except Exception as e:
        print(f"Error loading model: {str(e)}")
        print("Attempting to load with custom unpickler...")
        try:
            # Try loading with custom unpickler
            with open(model_path, 'rb') as f:
                model = joblib.load(f)
            with open(scaler_path, 'rb') as f:
                scaler = joblib.load(f)
            return model, scaler
        except Exception as e2:
            print(f"Second attempt failed: {str(e2)}")
            raise

# Load the enhanced models
model, scaler = load_model_with_fallback()

def preprocess(pw):
    return re.sub(r'[^a-zA-Z0-9]', '', pw.lower())

def predict_strength(password):
    try:
        features = extract_features(password)
        features_scaled = scaler.transform([features])
        pred = model.predict(features_scaled)[0]
        length, _, _, _, _, entropy, _, char_diversity, _ = features
        print(f"[DEBUG] Features: length={length}, entropy={entropy}, char_diversity={char_diversity}")
        # Improved hybrid override
        if (length >= 12 and entropy >= 3.3 and char_diversity >= 0.75) or (length >= 14 and char_diversity >= 0.7):
            print("[DEBUG] Hybrid override: classified as Very Strong")
            return 4  # Very Strong
        if hasattr(model, 'predict_proba'):
            proba = model.predict_proba(features_scaled)[0]
            print(f"[DEBUG] ML Prediction: {pred}, Probabilities: {proba}")
        else:
            print(f"[DEBUG] ML Prediction: {pred}")
        return int(pred)
    except Exception as e:
        print(f"Error during prediction: {str(e)}")
        raise

# In the debug output, the ML Prediction is the class (0-4), and Probabilities is the model's confidence for each class.
