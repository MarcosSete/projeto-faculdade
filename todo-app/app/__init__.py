"""
Inicialização da aplicação Flask.
Aqui é onde "montamos" o padrão MVC:
- Model  -> app/models.py (classe Tarefa + SQLAlchemy)
- View   -> app/templates/*.html (Jinja2)
- Controller -> app/routes.py (funções que recebem a requisição e decidem o que fazer)
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__)

    # Banco de dados SQLite. É um SGBD leve, gratuito e muito popular
    # (não é uma tecnologia obscura), perfeito para projetos pequenos/médios.
    base_dir = os.path.abspath(os.path.dirname(__file__))
    default_db_path = os.path.join(base_dir, "..", "instance", "tarefas.db")

    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{default_db_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "chave-simples-para-projeto-academico"

    if test_config:
        app.config.update(test_config)

    os.makedirs(os.path.join(base_dir, "..", "instance"), exist_ok=True)

    db.init_app(app)

    from . import routes
    app.register_blueprint(routes.bp)

    with app.app_context():
        db.create_all()

    return app
