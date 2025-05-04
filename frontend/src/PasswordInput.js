import React from "react";

function PasswordInput({ password, setPassword, handleSubmit, loading }) {
  return (
    <div className="password-input">
      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Enter your password"
        disabled={loading}
      />
      <button
        onClick={handleSubmit}
        disabled={loading || password.length === 0}
      >
        {loading ? "Analyzing..." : "Analyze"}
      </button>
    </div>
  );
}

export default PasswordInput;
