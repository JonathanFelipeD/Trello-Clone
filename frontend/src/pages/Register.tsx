import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import api from '../services/api'

export default function Register() {
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const navigate = useNavigate()

  async function handleRegister() {
    try {
      await api.post('/auth/register', { name, email, password })
      navigate('/login')
    } catch {
      setError('Erro ao criar conta')
    }
  }

  return (
    <div>
      <h1>Cadastro</h1>
      {error && <p>{error}</p>}
      <input
        type="text"
        placeholder="Nome"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
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
      <button onClick={handleRegister}>Cadastrar</button>
      <p>Já tem conta? <a href="/login">Entrar</a></p>
    </div>
  )
}