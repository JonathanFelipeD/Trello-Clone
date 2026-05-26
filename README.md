# Trello-Clone

Aplicação de gerenciamento de tarefas inspirada no Trllo, desenvolvida com Python (FastAPI) no backend e react no frontend.

# Tecnologias

- Python 3.14
- FastAPI
- SQLAlchemy
- PostgreSQL
- React

## Pré-requisitos

Antes de começar, instale na sua máquina:

- [Python 3.14](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/windows/)
- [Git](https://git-scm.com/downloads)
- [VSCode](https://code.visualstudio.com/)

## Instalação

1. Clone o repositório
```bash
git clone https://github.com/JonathanFelipeD/Trello-Clone.git
cd Trello-Clone
```

2. Crie e ative o ambiente virtual
```bash
cd backend
python -m venv venv
source venv/Scripts/activate
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

4. Configure o arquivo de variáveis de ambiente
- Crie um arquivo `.env` dentro da pasta `backend`
- Copie o conteúdo abaixo e preencha com suas credenciais

```env
DATABASE_URL=postgresql://postgres:SUA_SENHA@localhost:5432/trello_clone
JWT_SECRET=sua_chave_secreta
```

## Como rodar

1. Certifique-se que o PostgreSQL está rodando na sua máquina

2. Crie o banco de dados `trello_clone` no pgAdmin

3. Ative o ambiente virtual
```bash
cd backend
source venv/Scripts/activate
```

4. Suba o servidor
```bash
uvicorn app.main:app --reload
```

5. Acesse no navegador
- API: http://127.0.0.1:8000
- Documentação: http://127.0.0.1:8000/docs

## Fluxo de Branches

- `main` — código estável, não commitar direto
- `feature/nome-da-feature` — cada funcionalidade nova ganha uma branch própria

### Como criar uma branch nova
```bash
git checkout -b feature/nome-da-feature
```

### Como subir o código
```bash
git add .
git commit -m "feat: descrição do que foi feito"
git push origin feature/nome-da-feature
```

### Padrão de commits
- `feat:` nova funcionalidade
- `fix:` correção de bug
- `docs:` alteração em documentação
- `refactor:` refatoração de código


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
└── frontend/
    └── src/
        ├── components/   # Componentes reutilizáveis
        ├── pages/        # Telas da aplicação
        └── services/     # Chamadas à API
```