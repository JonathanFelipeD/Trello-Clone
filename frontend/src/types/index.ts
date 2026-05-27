export interface User {
    id: string
    name: string
    email: string
    role: string
}

export interface Board {
    id: string
    name: string
    description: string | null
    owner_id: string
    createdAt: string
}

export interface List {
    id: string
    board_id: string
    name: string
    position: number
    created_at: string
}

export interface Card {
  id: string
  list_id: string
  title: string
  description: string | null
  position: number
  priority: string
  assigned_to: string | null
  due_date: string | null
  status: string
  created_at: string
  updated_at: string
}

