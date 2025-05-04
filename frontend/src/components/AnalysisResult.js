import React from 'react';

function AnalysisResult({ result }) {
    if (!result) return null;
    return (
        <div className="analysis-result">
            <p><strong>Normalized:</strong> {result.normalized}</p>
            <p><strong>Semantic Matches:</strong> {result.semantic.join(', ')}</p>
            <p><strong>Context:</strong> {JSON.stringify(result.context)}</p>
            <p><strong>Heuristic Score:</strong> {result.heuristic_strength}</p>
            <p><strong>ML Prediction:</strong> {['Weak', 'Medium', 'Strong'][result.ml_prediction]}</p>
        </div>
    );
}

export default AnalysisResult;
