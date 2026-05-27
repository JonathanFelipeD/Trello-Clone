import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { useAuth } from '../contexts/AuthContext'
import api from '../services/api'
import type { Board } from '../types'

export default function Boards() {
  const [boards, setBoards] = useState<Board[]>([])
  const [name, setName] = useState('')
  const [description, setDescription] = useState('')
  const { logout } = useAuth()
  const navigate = useNavigate()

  useEffect(() => {
    fetchBoards()
  }, [])

  async function fetchBoards() {
    try {
      const response = await api.get('/boards/')
      setBoards(response.data)
    } catch {
      console.error('Erro ao buscar boards')
    }
  }

  async function handleCreateBoard() {
    try {
      await api.post('/boards/', { name, description })
      setName('')
      setDescription('')
      fetchBoards()
    } catch {
      console.error('Erro ao criar board')
    }
  }

  return (
    <div>
      <h1>Meus Boards</h1>
      <button onClick={logout}>Sair</button>
      <div>
        <input
          type="text"
          placeholder="Nome do board"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <input
          type="text"
          placeholder="Descrição"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
        <button onClick={handleCreateBoard}>Criar Board</button>
      </div>
      <div>
        {boards.map(board => (
          <div key={board.id} onClick={() => navigate(`/boards/${board.id}`)}>
            <h2>{board.name}</h2>
            <p>{board.description}</p>
          </div>
        ))}
      </div>
    </div>
  )
}