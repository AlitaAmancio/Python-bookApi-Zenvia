# Python-bookApi-Zenvia
API RESTful para livros usando Flask, SQLAlchemy e PostgreSQL. Desenvolvida em [Python](https://www.python.org/) como aquecimento para o processo de estágio da empresa Zenvia.

## Instalação

#### 1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/python-books-api.git
   cd python-books-api
   ```

   
#### 2. Crie um ambiente virtual e ative-o:
  ```sh
  python -m venv venv
  source venv/bin/activate  # No Windows use `venv\Scripts\activate`
  ```

#### 3. Instale as Dependências:
  ```sh
  pip install -r requirements.txt
  ```

#### 4. Copie o arquivo .env.example para .env e edite-o com suas configurações:
  ```sh
  cp .env.example .env  # No Windows use `copy .env.example .env`

  ```

#### 5. Aesse o PostgreSQL com seu cliente de banco de dados preferido e crie um banco de dados:
  ```sql
  CREATE DATABASE python_books;
  ```

#### 6. Configure o banco de dados no arquivo `.env`, substituindo o usuario e senha pelos seus valores:
  ```sh
  DATABASE_URL=postgresql://postgres:senha@localhost:5432/python_books
  ```

#### 7. Execute as migrações para criar as tabelas no banco de dados:
  ```sh
  flask db init
  flask db migrate
  flask db upgrade
  ```

#### 8. Inicie a aplicação:
  ```sh
  flask run
  ```
## Usando a aplicação
Para testar a API, você pode usar o Postman ou qualquer outra ferramenta similar. Abaixo estão as rotas disponíveis e exemplos de como passar dados em formato JSON:

### Rotas da API

#### 1. Obter todos os livros

- **Rota:** `GET /books/`
- **Resposta:** Lista de todos os livros.

#### 2. Obter um livro por ID

- **Rota:** `GET /books/<int:id>`
- **Resposta:** Dados do livro com o ID especificado.

#### 3. Criar um novo livro

- **Rota:** `POST /books/`
- **Exemplo de JSON para requisição:**

  ```json
  {
      "title": "Exemplo de Livro",
      "author": "Autor Exemplo",
      "published_date": "2024-01-01",
      "isbn": "1234567890123"
  }
  ```

#### 4. Atualizar um livro
- **Rota:** `PUT /books/<int:id>`
- **Exemplo de JSON para requisição:**

 ```json
{
    "title": "Livro Atualizado",
    "author": "Autor Atualizado",
    "published_date": "2024-01-02",
    "isbn": "1234567890123"
}
  ```

#### 5. Deletar um livro
- **Rota:** `DELETE /books/<int:id>`
- **Resposta:** Código de status 204 (No Content).

## Dependências

- Flask
- Python-dotenv
- Psycopg2-binary
- Flask-SQLAlchemy
- Flask-Migrate

## Variáveis de Ambiente

- `DATABASE_URL`: URL de conexão com o banco de dados PostgreSQL.
- `FLASK_APP`: Nome do módulo Flask.
- `FLASK_DEBUG`: Modo de depuração.

## Comandos Úteis

- `flask run`: Inicia a aplicação.
- `flask db init`: Inicializa o diretório de migrações.
- `flask db migrate`: Cria uma nova migração.
- `flask db upgrade`: Aplica as migrações ao banco de dados.



