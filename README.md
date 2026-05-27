# Trello Clone

Aplicação de gerenciamento de tarefas inspirada no Trello, desenvolvida com Python (FastAPI) no backend e React + TypeScript no frontend.

---

## Tecnologias

### Backend
- Python 3.14
- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT (autenticação)
- Bcrypt (criptografia de senha)

### Frontend
- React + TypeScript (Vite)
- Axios
- React Router DOM
- DND Kit (drag and drop)

---

## Pré-requisitos

Antes de começar, instale na sua máquina:

- [Python 3.14](https://www.python.org/downloads/)
- [Node.js 18+](https://nodejs.org/)
- [PostgreSQL](https://www.postgresql.org/download/windows/)
- [Git](https://git-scm.com/downloads)
- [VSCode](https://code.visualstudio.com/)

---

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/JonathanFelipeD/Trello-Clone.git
cd Trello-Clone
```

### 2. Configure o Backend

```bash
cd backend
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

Crie um arquivo `.env` dentro da pasta `backend` com o seguinte conteúdo:

```env
DATABASE_URL=postgresql://postgres:SUA_SENHA@localhost:5432/trello_clone
JWT_SECRET=sua_chave_secreta
```

> Substitua `SUA_SENHA` pela senha que você definiu na instalação do PostgreSQL.

### 3. Configure o banco de dados

- Abra o pgAdmin
- Crie um banco de dados chamado `trello_clone`
- As tabelas são criadas automaticamente quando o servidor sobe

### 4. Configure o Frontend

```bash
cd ../frontend
npm install
```

---

## Como rodar

### Backend

```bash
cd backend
source venv/Scripts/activate
uvicorn app.main:app --reload
```

Acesse:
- API: http://127.0.0.1:8000
- Documentação interativa: http://127.0.0.1:8000/docs

### Frontend

```bash
cd frontend
npm run dev
```

Acesse:
- Frontend: http://localhost:5173

---

## Estrutura de Pastas

```
Trello-Clone/
├── backend/
│   ├── app/
│   │   ├── models/       # Tabelas do banco de dados
│   │   ├── routers/      # Endpoints da API
│   │   ├── schemas/      # Validação de dados
│   │   ├── services/     # Lógica de negócio
│   │   ├── database.py   # Configuração do banco
│   │   └── main.py       # Ponto de entrada da API
│   ├── .env              # Variáveis de ambiente (não sobe pro GitHub)
│   └── requirements.txt  # Dependências do projeto
├── frontend/
│   └── src/
│       ├── components/   # Componentes reutilizáveis
│       ├── contexts/     # Estado global (autenticação)
│       ├── pages/        # Telas da aplicação
│       ├── services/     # Chamadas à API
│       └── types/        # Tipos TypeScript
├── CHANGELOG.md
├── PROGRESS.md
└── README.md
```

---

## Fluxo de Trabalho Git

- `main` — código estável, não commitar direto
- `feature/nome-da-feature` — cada funcionalidade nova ganha uma branch própria

### Criar uma branch nova

```bash
git checkout -b feature/nome-da-feature
```

### Subir o código

```bash
git add .
git commit -m "feat: descrição do que foi feito"
git push origin feature/nome-da-feature
```

### Sincronizar com a main

```bash
git checkout feature/sua-branch
git pull origin main
```

### Padrão de commits

| Prefixo | Uso |
|--------|-----|
| `feat:` | Nova funcionalidade |
| `fix:` | Correção de bug |
| `docs:` | Alteração em documentação |
| `refactor:` | Refatoração de código |
| `style:` | Formatação, sem mudança de lógica |

---

## Rotas da API

### Auth
| Método | Rota | Descrição |
|--------|------|-----------|
| POST | /auth/register | Cadastro de usuário |
| POST | /auth/login | Login e geração de token |

### Boards
| Método | Rota | Descrição |
|--------|------|-----------|
| GET | /boards/ | Listar boards do usuário |
| POST | /boards/ | Criar novo board |

### Lists
| Método | Rota | Descrição |
|--------|------|-----------|
| GET | /boards/{board_id}/lists/ | Listar listas de um board |
| POST | /boards/{board_id}/lists/ | Criar nova lista |

### Cards
| Método | Rota | Descrição |
|--------|------|-----------|
| GET | /lists/{list_id}/cards/ | Listar cards de uma lista |
| POST | /lists/{list_id}/cards/ | Criar novo card |