# Changelog

## [0.1.0] - 26/05/2026

### Adicionado
- Estrutura inicial do projeto (backend e frontend)
- Configuração do ambiente Python com venv
- Instalação das dependências (FastAPI, SQLAlchemy, PostgreSQL, JWT, bcrypt)
- Configuração do banco de dados PostgreSQL
- Models: User, Board, List, Card
- Configuração da conexão com o banco (database.py)
- Sistema de autenticação completo:
  - Registro de usuário com senha criptografada (bcrypt)
  - Login com geração de token JWT
  - Schemas de validação de dados (UserCreate, UserResponse)


## [0.2.0] - 27/05/2026

### Adicionado
- CRUD completo de Boards
- CRUD completo de Lists
- CRUD completo de Cards
- Autenticação via JWT nas rotas protegidas


## [0.3.0] - 27/05/2026

### Adicionado
- Configuração do frontend com Vite + React + TypeScript
- Instalação das bibliotecas: axios, react-router-dom, dnd-kit
- Estrutura de pastas do frontend (components, pages, services, types, contexts)
- Tipos TypeScript para User, Board, List e Card
- Serviço de API com axios e interceptor de autenticação
- Context de autenticação (login, logout, token persistido no localStorage)