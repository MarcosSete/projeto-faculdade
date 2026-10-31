"""
Testes automatizados (pytest) do back-end.
Cobrem as operações de CRUD (Create, Read, Update, Delete) da entidade Tarefa.
Estes testes servem como parte da VERIFICAÇÃO do sistema (Situação-Problema 3:
"Realizar e documentar os testes - verificação e validação").
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from app import create_app, db
from app.models import Tarefa


@pytest.fixture
def client():
    app = create_app(test_config={
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "TESTING": True,
    })
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client


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
    }, follow_redirects=True)

    assert "obrigatório".encode() in resposta.data


def test_editar_tarefa(client):
    client.post("/nova", data={"titulo": "Tarefa original"})
    with client.application.app_context():
        tarefa = Tarefa.query.first()
        tarefa_id = tarefa.id

    resposta = client.post(f"/editar/{tarefa_id}", data={
        "titulo": "Tarefa editada",
        "descricao": "",
        "status": "Pendente",
    }, follow_redirects=True)

    assert "Tarefa editada".encode() in resposta.data


def test_concluir_tarefa_alterna_status(client):
    client.post("/nova", data={"titulo": "Tarefa para concluir"})
    with client.application.app_context():
        tarefa = Tarefa.query.first()
        tarefa_id = tarefa.id
        assert tarefa.status == "Pendente"

    client.post(f"/concluir/{tarefa_id}", follow_redirects=True)

    with client.application.app_context():
        tarefa = Tarefa.query.get(tarefa_id)
        assert tarefa.status == "Concluída"


def test_excluir_tarefa(client):
    client.post("/nova", data={"titulo": "Tarefa para excluir"})
    with client.application.app_context():
        tarefa_id = Tarefa.query.first().id

    client.post(f"/excluir/{tarefa_id}", follow_redirects=True)

    with client.application.app_context():
        assert Tarefa.query.get(tarefa_id) is None


def test_tarefa_inexistente_retorna_404(client):
    resposta = client.get("/editar/9999")
    assert resposta.status_code == 404
