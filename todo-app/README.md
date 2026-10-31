# Gerenciador de Tarefas — PIT em Engenharia de Software II

Aplicação web simples de lista de tarefas (To-Do List), construída para o
Projeto Integrador Transdisciplinar em Engenharia de Software II.

## Stack utilizada

| Camada | Tecnologia |
|---|---|
| Front-end (View) | HTML5 + CSS + Jinja2 (templates do Flask) |
| Back-end (Controller) | Python 3 + Flask |
| Model | SQLAlchemy (ORM) |
| Banco de dados | SQLite |
| Testes | Pytest |
| Padrão arquitetural | MVC (Model-View-Controller) |

## Estrutura de pastas (mapeada ao MVC)

```
todo-app/
├── app/
│   ├── __init__.py       # cria e configura a aplicação Flask
│   ├── models.py         # MODEL: classe Tarefa (SQLAlchemy)
│   ├── routes.py         # CONTROLLER: rotas/lógica de negócio
│   ├── templates/        # VIEW: páginas HTML (Jinja2)
│   └── static/style.css  # estilos
├── tests/
│   └── test_app.py       # testes automatizados (pytest)
├── docs/
│   ├── diagrama_de_classes.md
│   ├── DER.md
│   ├── dicionario_de_dados.md
│   └── schema.sql
├── run.py                # ponto de entrada da aplicação
└── requirements.txt
```

## Como rodar o projeto localmente

1. Tenha o Python 3.10+ instalado.
2. Crie um ambiente virtual (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Rode a aplicação:
   ```bash
   python run.py
   ```
5. Acesse no navegador: **http://127.0.0.1:5000**

O banco de dados SQLite (`instance/tarefas.db`) é criado automaticamente na
primeira execução — não é preciso instalar nenhum servidor de banco de dados.

## Como rodar os testes automatizados

```bash
pytest tests/ -v
```

Isso executa os testes de criação, leitura, edição, exclusão e alteração de
status das tarefas (cobrindo o CRUD completo do back-end).

## Funcionalidades

- Criar tarefa (título, descrição, data de vencimento)
- Listar todas as tarefas
- Editar tarefa
- Marcar como concluída / reabrir
- Excluir tarefa
- Validação: título é obrigatório (mensagem de erro amigável)

## Documentação do projeto

- [Diagrama de Classes](docs/diagrama_de_classes.md)
- [Diagrama Entidade-Relacionamento (DER)](docs/DER.md)
- [Dicionário de Dados](docs/dicionario_de_dados.md)
- [Projeto físico do banco (schema.sql)](docs/schema.sql)

## Como publicar no GitHub (passo a passo)

1. Crie uma conta em https://github.com (se ainda não tiver).
2. Crie um novo repositório (botão **New repository**), por exemplo
   `pit-engenharia-software-2`. Deixe-o **público**.
3. No seu computador, dentro da pasta `todo-app`, rode:
   ```bash
   git init
   git add .
   git commit -m "Primeira versão do Gerenciador de Tarefas"
   git branch -M main
   git remote add origin https://github.com/SEU-USUARIO/pit-engenharia-software-2.git
   git push -u origin main
   ```
4. Copie o link do repositório e cole no seu documento de entrega.

