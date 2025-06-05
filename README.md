# estudo_python

Este projeto é um exemplo simples de aplicação **FastAPI** seguindo princípios de arquitetura limpa.
Ele utiliza SQLite como banco de dados e demonstra a separação de camadas de domínio,
aplicação, infraestrutura e interface web.

## Estrutura
- `domain` – entidades e serviços de domínio
- `application` – esquemas e serviços de aplicação
- `infrastructure` – acesso a banco de dados e repositórios
- `interfaces` – camadas de API

## Requisitos
Python 3.11 ou superior é recomendado. Instale as dependências em um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Executando a aplicação
Após instalar as dependências, inicialize o servidor com:

```bash
uvicorn main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000` e inclui documentação automática em
`/docs`.

## Principais endpoints
Os testes utilizam as rotas abaixo para criar e consultar usuários:

- `POST /users/` – cria um novo usuário
- `GET /users/` – lista todos os usuários
- `GET /users/{id}` – obtém um usuário pelo identificador

## Testes
O projeto contém testes unitários e funcionais escritos com **pytest**. Para executá-los:

```bash
pytest
```

Os testes cobrem a camada de domínio, a camada de aplicação e as rotas expostas pela API.
