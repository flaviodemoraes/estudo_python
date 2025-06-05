# estudo_python

Projeto de exemplo usando FastAPI com arquitetura limpa.

## Estrutura
- `domain`  – entidades e servicos de dominio
- `application` – schemas e servicos de aplicacao
- `infrastructure` – acesso a banco de dados e repositorios
- `interfaces` – camadas de API

## Executando
Crie um ambiente virtual e instale `fastapi` e `sqlalchemy` (além do `uvicorn`).

```bash
uvicorn main:app --reload
```
