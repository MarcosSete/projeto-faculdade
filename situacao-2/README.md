# Situação 2 — Desenvolvimento

| Item | Detalhe |
|---|---|
| Front-end | HTML, CSS e templates Jinja2 — `todo-app/app/templates/` e `todo-app/app/static/` |
| Back-end | Python + Flask — `todo-app/app/routes.py` |
| Model | SQLAlchemy — `todo-app/app/models.py` |
| Padrão | MVC |
| Banco | SQLite |
| Testes automatizados | pytest — `todo-app/tests/test_app.py` |
| Modo de codificação | Tradicional (sem low-code/no-code) |

## Como executar
Veja o [README do código](../todo-app/README.md).

## Como rodar os testes
```bash
cd todo-app
pip install -r requirements.txt
pytest tests/ -v
```

## Entregas
- Código no GitHub: pasta [`todo-app/`](../todo-app/)
- Manual de uso: [`manual_de_uso.md`](../manual_de_uso.md)
- Vídeo de demonstração: ver [`situacao-3/videos.md`](../situacao-3/videos.md)
