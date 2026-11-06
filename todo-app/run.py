"""Ponto de entrada para execução local e Gunicorn."""
import os

if __name__ == "__main__":
    # Chave apenas para desenvolvimento local. Em produção, configure SECRET_KEY.
    os.environ.setdefault("SECRET_KEY", "chave-local-apenas-para-desenvolvimento")

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
