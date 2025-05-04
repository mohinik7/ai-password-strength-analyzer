import React from 'react';

function PasswordInput({ password, setPassword, handleSubmit }) {
    return (
        <div className="password-input">
            <input
                type="text"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Enter your password"
            />
            <button onClick={handleSubmit}>Analyze</button>
        </div>
    );
}

export default PasswordInput;
