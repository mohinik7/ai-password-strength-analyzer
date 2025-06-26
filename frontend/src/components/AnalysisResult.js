import React from 'react';

const strengthLabels = ['Very Weak', 'Weak', 'Medium', 'Strong', 'Very Strong'];

function AnalysisResult({ result }) {
    if (!result) return null;
    return (
        <div className="analysis-result">
            <p><strong>Normalized:</strong> {result.normalized}</p>
            <p><strong>Heuristic Score:</strong> {result.heuristic_strength}</p>
            <p><strong>ML Prediction:</strong> {strengthLabels[result.ml_prediction]}</p>
        </div>
    );
}

export default AnalysisResult;
