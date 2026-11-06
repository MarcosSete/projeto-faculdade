"""Inicialização e configuração da aplicação Flask."""
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
csrf = CSRFProtect()


def create_app(test_config=None):
    app = Flask(__name__)

    # Em produção, SECRET_KEY deve ser configurada nas variáveis de ambiente.
    secret_key = os.environ.get("SECRET_KEY")
    if test_config:
        secret_key = test_config.get("SECRET_KEY", secret_key)
    if not secret_key:
        raise RuntimeError(
            "Configure a variável de ambiente SECRET_KEY antes de iniciar a aplicação."
        )

    base_dir = os.path.abspath(os.path.dirname(__file__))
    instance_dir = os.path.abspath(os.path.join(base_dir, "..", "instance"))
    os.makedirs(instance_dir, exist_ok=True)

    default_db_path = os.path.join(instance_dir, "tarefas.db")
    app.config.update(
        SECRET_KEY=secret_key,
        SQLALCHEMY_DATABASE_URI=os.environ.get(
            "DATABASE_URL", f"sqlite:///{default_db_path}"
        ),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        MAX_CONTENT_LENGTH=1024 * 1024,  # 1 MB por requisição
    )

    if test_config:
        app.config.update(test_config)

    db.init_app(app)
    csrf.init_app(app)

    from . import routes
    app.register_blueprint(routes.bp)

    with app.app_context():
        db.create_all()

    return app
