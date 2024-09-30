import React, { useState } from "react";
import axios from "axios";

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
    <div>
      <h2>Login</h2>
      <form onSubmit={handleLogin}>
        <div>
          <label>Username:</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>
        <div>
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <button type="submit">Login</button>
      </form>
      {token && <p>Logged in! Token: {token}</p>}
    </div>
  );
}

export default Login;