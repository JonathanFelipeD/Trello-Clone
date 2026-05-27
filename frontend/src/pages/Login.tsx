import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext'
import api from '../services/api'

export default function Login(){
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const { login } = useAuth();
    const navigate = useNavigate();

    async function handleLogin() {
      try {
        const response = await api.post('/auth/login', { email, password })
        const token = response.data.access_token
        localStorage.setItem('token', token)
        login(token, { id: '', name: '', email, role: 'member' })
        navigate('/boards')
      } catch {
        setError('Email ou senha incorretos')
      }

    }

    return (
        <div>
      <h1>Login</h1>
      {error && <p>{error}</p>}
      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <input
        type="password"
        placeholder="Senha"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button onClick={handleLogin}>Entrar</button>
      <p>Não tem conta? <a href="/register">Cadastre-se</a></p>
    </div>
    )
}