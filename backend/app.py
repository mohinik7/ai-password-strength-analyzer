from flask import Flask, request, jsonify
from flask_cors import CORS  # Add CORS support
from normalizer import normalize_password
# from semantic_analyzer import semantic_match  # Removed
# from context_parser import parse_context  # Removed
from strength_evaluator import evaluate_strength
from ml_model import predict_strength

app = Flask(__name__)
CORS(app)  # Enable CORS so frontend can connect


@app.route('/api/analyze', methods=['POST'])  # Use correct route
def analyze():
    data = request.get_json()
    if not data or "password" not in data:
        return jsonify({"error": "Missing 'password' in request"}), 400

    password = data["password"]

    normalized = normalize_password(password)
    # semantic = semantic_match(normalized)  # Removed
    # context = parse_context(normalized)    # Removed
    heuristic_score = evaluate_strength(normalized)
    ml_prediction = predict_strength(normalized)

    return jsonify({
        "normalized": normalized,
        # "semantic": semantic,  # Removed
        # "context": context,    # Removed
        "heuristic_strength": heuristic_score,
        "ml_prediction": ml_prediction
    })


if __name__ == '__main__':
    app.run(debug=True)
