def evaluate_strength(password):
    length_score = min(len(password), 12) / 12
    variety_score = len(set(password)) / len(password) if password else 0
    score = 0.5 * length_score + 0.5 * variety_score
    return round(score * 100, 2)
