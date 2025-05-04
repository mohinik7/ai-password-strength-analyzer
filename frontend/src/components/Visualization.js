import React from 'react';

function Visualization({ score }) {
    return (
        <div className="visualization">
            <p>Password Strength: {score}%</p>
            <progress value={score} max="100" />
        </div>
    );
}

export default Visualization;
