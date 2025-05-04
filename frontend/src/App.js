import React, { useState } from "react";
import PasswordInput from "./components/PasswordInput";
import AnalysisResult from "./components/AnalysisResult";
import Visualization from "./components/Visualization";

function App() {
  const [password, setPassword] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    // Clear previous results and errors
    setError(null);
    setLoading(true);

    try {
      const response = await fetch("http://localhost:5000/api/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ password }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      console.error("Failed to analyze password:", err);
      setError(
        "Failed to connect to server. Make sure the backend is running on port 5000."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>Password Strength Analyzer</h1>
      <PasswordInput
        password={password}
        setPassword={setPassword}
        handleSubmit={handleSubmit}
        loading={loading}
      />

      {error && (
        <div
          className="error-message"
          style={{ color: "red", marginTop: "10px" }}
        >
          {error}
        </div>
      )}

      <Visualization score={result ? result.heuristic_strength : 0} />
      <AnalysisResult result={result} />
    </div>
  );
}

export default App;
