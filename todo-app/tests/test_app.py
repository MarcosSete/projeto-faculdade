"""Testes automatizados das rotas e regras básicas da aplicação."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest

from app import create_app, db
from app.models import Tarefa


@pytest.fixture
def client():
    app = create_app(test_config={
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SECRET_KEY": "chave-de-teste",
        "TESTING": True,
        "WTF_CSRF_ENABLED": False,
    })
    with app.app_context():
        db.create_all()
    with app.test_client() as test_client:
        yield test_client
    with app.app_context():
        db.session.remove()
        db.drop_all()


def test_pagina_inicial_carrega(client):
    resposta = client.get("/")
    assert resposta.status_code == 200
    assert "Gerenciador de Tarefas".encode() in resposta.data


def test_criar_tarefa(client):
    resposta = client.post("/nova", data={
        "titulo": "Estudar para a prova",
        "descricao": "Revisar UML e banco de dados",
        "data_vencimento": "2026-12-01",
    }, follow_redirects=True)
    assert resposta.status_code == 200
    assert "Estudar para a prova".encode() in resposta.data


def test_criar_tarefa_sem_titulo_falha(client):
    resposta = client.post("/nova", data={
        "titulo": "",
        "descricao": "Sem título",
    })
    assert resposta.status_code == 400
    assert "obrigatório".encode() in resposta.data


def test_editar_tarefa(client):
    client.post("/nova", data={"titulo": "Tarefa original"})
    with client.application.app_context():
        tarefa_id = Tarefa.query.first().id
    resposta = client.post(f"/editar/{tarefa_id}", data={
        "titulo": "Tarefa editada",
        "descricao": "",
        "status": "Pendente",
    }, follow_redirects=True)
    assert resposta.status_code == 200
    assert "Tarefa editada".encode() in resposta.data


def test_concluir_tarefa_alterna_status(client):
    client.post("/nova", data={"titulo": "Tarefa para concluir"})
    with client.application.app_context():
        tarefa_id = Tarefa.query.first().id
    client.post(f"/concluir/{tarefa_id}", follow_redirects=True)
    with client.application.app_context():
        assert db.session.get(Tarefa, tarefa_id).status == "Concluída"


def test_excluir_tarefa(client):
    client.post("/nova", data={"titulo": "Tarefa para excluir"})
    with client.application.app_context():
        tarefa_id = Tarefa.query.first().id
    client.post(f"/excluir/{tarefa_id}", follow_redirects=True)
    with client.application.app_context():
        assert db.session.get(Tarefa, tarefa_id) is None


def test_tarefa_inexistente_retorna_404(client):
    resposta = client.get("/editar/9999")
    assert resposta.status_code == 404


def test_data_invalida_nao_gera_erro_500(client):
    resposta = client.post("/nova", data={
        "titulo": "Tarefa com data inválida",
        "data_vencimento": "2026-99-99",
    })
    assert resposta.status_code == 400
    assert "data de vencimento válida".encode() in resposta.data


def test_titulo_acima_do_limite_e_rejeitado(client):
    resposta = client.post("/nova", data={"titulo": "T" * 121})
    assert resposta.status_code == 400


def test_descricao_acima_do_limite_e_rejeitada(client):
    resposta = client.post("/nova", data={
        "titulo": "Tarefa",
        "descricao": "D" * 501,
    })
    assert resposta.status_code == 400


def test_status_invalido_e_rejeitado(client):
    client.post("/nova", data={"titulo": "Tarefa"})
    with client.application.app_context():
        tarefa_id = Tarefa.query.first().id
    resposta = client.post(f"/editar/{tarefa_id}", data={
        "titulo": "Tarefa",
        "status": "Qualquer valor",
    })
    assert resposta.status_code == 400
    with client.application.app_context():
        assert db.session.get(Tarefa, tarefa_id).status == "Pendente"


def test_concluir_tarefa_inexistente_retorna_404(client):
    resposta = client.post("/concluir/9999")
    assert resposta.status_code == 404


def test_excluir_tarefa_inexistente_retorna_404(client):
    resposta = client.post("/excluir/9999")
    assert resposta.status_code == 404
