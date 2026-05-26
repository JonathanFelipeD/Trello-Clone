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