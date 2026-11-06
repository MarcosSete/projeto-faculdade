# Gerenciador de Tarefas — PIT em Engenharia de Software II

Aplicação web simples de lista de tarefas (To-Do List), construída para o Projeto Integrador Transdisciplinar em Engenharia de Software II.

## Stack utilizada
| Camada | Tecnologia |
|---|---|
| Front-end (View) | HTML5 + CSS + Jinja2 (templates do Flask) |
| Back-end (Controller) | Python 3 + Flask |
| Model | SQLAlchemy (ORM) |
| Banco de dados | SQLite |
| Testes | Pytest |
| Padrão arquitetural | MVC (Model-View-Controller) |

## Estrutura de pastas
```
todo-app/
├── app/                 # Model, Controller, templates e estilos
├── tests/test_app.py    # testes automatizados (pytest)
├── docs/                # diagramas, dicionário, formulário e schema
├── run.py               # ponto de entrada
└── requirements.txt
```

## Como rodar localmente
1. Tenha Python 3.10+ instalado.
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```
3. Instale as dependências: `pip install -r requirements.txt`.
4. Execute: `python run.py`.
5. Acesse http://127.0.0.1:5000.

O banco SQLite (`instance/tarefas.db`) é criado automaticamente na primeira execução.

## Testes automatizados
```bash
pytest tests/ -v
```
Os testes cobrem criação, listagem, edição, exclusão, alteração de status, validação do título obrigatório e resposta 404.

## Funcionalidades
- Criar tarefa (título, descrição e data de vencimento).
- Listar tarefas.
- Editar tarefa.
- Marcar como concluída ou reabrir.
- Excluir tarefa.
- Validar o preenchimento obrigatório do título.

## Documentação
- [Diagrama de Classes](docs/diagrama_de_classes.md)
- [Diagrama Entidade-Relacionamento (DER)](docs/DER.md)
- [Dicionário de Dados](docs/dicionario_de_dados.md)
- [Projeto físico do banco (schema.sql)](docs/schema.sql)

## Hospedagem (opcional)
O projeto pode ser publicado no Render. Configure:
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn run:app`

O plano gratuito pode suspender o serviço após inatividade; o primeiro acesso pode demorar. O armazenamento local SQLite pode não ser persistente entre reinicializações.
