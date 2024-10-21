import React, { useState } from "react";
import axios from "axios";
import './Login.css';  // Importa los estilos

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [token, setToken] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://localhost:8000/token", {
        username: username,
        password: password,
      }, {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded"
        },
      });

      // Guardar el token
      setToken(response.data.access_token);
      console.log("Token:", response.data.access_token);

    } catch (error) {
      console.error("Error en el login:", error);
    }
  };

  return (
    <div className="login-container">
      <div className="login-box">
        <div className="app-header">
          <img src="/Quinielas-logo.jpg" alt="App Logo" className="app-logo"/>
          <h1 className="app-name">Quinielas Oscarin</h1>
        </div>

        <h2>Login</h2>
        <form onSubmit={handleLogin}>
          <div className="input-group">
            <label>Username:</label>
            <input
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Enter your username"
            />
          </div>
          <div className="input-group">
            <label>Password:</label>
            <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Enter your password"
            />
          </div>
          <button type="submit" className="login-button">Login</button>
        </form>
        {token && <p className="success-message">Logged in! Token: {token}</p>}
      </div>
    </div>
  );
}

export default Login;
