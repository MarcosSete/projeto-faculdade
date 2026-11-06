# Gerenciador de Tarefas — PIT em Engenharia de Software II

Aplicação web simples de lista de tarefas (To-Do List), construída para o Projeto Integrador Transdisciplinar em Engenharia de Software II.

## Stack utilizada
| Camada | Tecnologia |
|---|---|
| Front-end (View) | HTML5 + CSS + Jinja2 |
| Back-end (Controller) | Python 3 + Flask |
| Model | SQLAlchemy |
| Banco de dados | SQLite |
| Testes | Pytest |
| Padrão arquitetural | MVC |

## Como rodar localmente
1. Tenha Python 3.10+ instalado.
2. Entre na pasta `todo-app` e crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute:
   ```bash
   python run.py
   ```
5. Acesse http://127.0.0.1:5000.

O banco SQLite é criado automaticamente em `instance/tarefas.db`.

## Testes automatizados
Execute dentro de `todo-app`:
```bash
pytest tests/ -v
```

Os testes cobrem as operações CRUD, validações básicas, datas inválidas e respostas 404.

## Publicação no Render
Como o código está dentro da pasta `todo-app`, configure o serviço no Render assim:

- **Root Directory:** `todo-app`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn run:app`

Configure também a variável de ambiente `SECRET_KEY` com uma chave longa, aleatória e privada.

### Persistência do banco
O SQLite grava os dados em um arquivo. Em hospedagens com sistema de arquivos efêmero, os dados podem ser perdidos quando a instância é reiniciada ou recriada.

Para manter o SQLite no Render, associe um Persistent Disk ao serviço, com ponto de montagem `/var/data`, e configure:

```text
DATABASE_URL=sqlite:////var/data/tarefas.db
```

Sem disco persistente, a aplicação ainda pode iniciar e funcionar, mas não há garantia de que as tarefas permaneçam salvas após reinicializações. Para este projeto acadêmico, manter uma única instância com SQLite e disco persistente é suficiente; não é necessário adicionar uma arquitetura mais complexa.

## Funcionalidades
- Criar e listar tarefas.
- Editar tarefas.
- Marcar como concluída ou reabrir.
- Excluir tarefas.
- Validar título, descrição, status e data de vencimento.
- Proteger formulários contra envios CSRF.

## Documentação
- [Diagrama de Classes](docs/diagrama_de_classes.md)
- [Diagrama Entidade-Relacionamento (DER)](docs/DER.md)
- [Dicionário de Dados](docs/dicionario_de_dados.md)
- [Projeto físico do banco (schema.sql)](docs/schema.sql)
