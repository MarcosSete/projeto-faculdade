"""CONTROLLER: rotas e regras básicas do gerenciador de tarefas."""
from datetime import datetime

from flask import Blueprint, flash, redirect, render_template, request, url_for
from sqlalchemy.exc import SQLAlchemyError

from . import db
from .models import Tarefa

bp = Blueprint("routes", __name__)
STATUS_VALIDOS = {"Pendente", "Concluída"}


def _parse_data(valor):
    """Converte uma data HTML (AAAA-MM-DD), tratando entradas inválidas."""
    if not valor:
        return None
    try:
        return datetime.strptime(valor, "%Y-%m-%d").date()
    except ValueError as exc:
        raise ValueError("Informe uma data de vencimento válida.") from exc


def _validar_campos(titulo, descricao):
    if not titulo:
        return "O título é obrigatório."
    if len(titulo) > 120:
        return "O título deve ter no máximo 120 caracteres."
    if len(descricao) > 500:
        return "A descrição deve ter no máximo 500 caracteres."
    return None


def _commit_ou_rollback():
    try:
        db.session.commit()
    except SQLAlchemyError:
        db.session.rollback()
        raise


@bp.route("/")
def index():
    tarefas = Tarefa.query.order_by(Tarefa.data_criacao.desc()).all()
    return render_template("index.html", tarefas=tarefas)


@bp.route("/nova", methods=["GET", "POST"])
def nova_tarefa():
    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        descricao = request.form.get("descricao", "").strip()
        erro = _validar_campos(titulo, descricao)

        if erro:
            flash(erro, "erro")
            return render_template("form.html", tarefa=None), 400

        try:
            data_vencimento = _parse_data(request.form.get("data_vencimento", ""))
        except ValueError as exc:
            flash(str(exc), "erro")
            return render_template("form.html", tarefa=None), 400

        tarefa = Tarefa(
            titulo=titulo,
            descricao=descricao,
            data_vencimento=data_vencimento,
        )
        db.session.add(tarefa)
        _commit_ou_rollback()
        flash("Tarefa criada com sucesso!", "sucesso")
        return redirect(url_for("routes.index"))

    return render_template("form.html", tarefa=None)


@bp.route("/editar/<int:tarefa_id>", methods=["GET", "POST"])
def editar_tarefa(tarefa_id):
    tarefa = Tarefa.query.get_or_404(tarefa_id)

    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        descricao = request.form.get("descricao", "").strip()
        erro = _validar_campos(titulo, descricao)

        if erro:
            flash(erro, "erro")
            return render_template("form.html", tarefa=tarefa), 400

        novo_status = request.form.get("status", tarefa.status)
        if novo_status not in STATUS_VALIDOS:
            flash("Status inválido.", "erro")
            return render_template("form.html", tarefa=tarefa), 400

        try:
            data_vencimento = _parse_data(request.form.get("data_vencimento", ""))
        except ValueError as exc:
            flash(str(exc), "erro")
            return render_template("form.html", tarefa=tarefa), 400

        tarefa.titulo = titulo
        tarefa.descricao = descricao
        tarefa.status = novo_status
        tarefa.data_vencimento = data_vencimento
        _commit_ou_rollback()
        flash("Tarefa atualizada com sucesso!", "sucesso")
        return redirect(url_for("routes.index"))

    return render_template("form.html", tarefa=tarefa)


@bp.route("/concluir/<int:tarefa_id>", methods=["POST"])
def concluir_tarefa(tarefa_id):
    tarefa = Tarefa.query.get_or_404(tarefa_id)
    tarefa.status = "Concluída" if tarefa.status == "Pendente" else "Pendente"
    _commit_ou_rollback()
    return redirect(url_for("routes.index"))


@bp.route("/excluir/<int:tarefa_id>", methods=["POST"])
def excluir_tarefa(tarefa_id):
    tarefa = Tarefa.query.get_or_404(tarefa_id)
    db.session.delete(tarefa)
    _commit_ou_rollback()
    flash("Tarefa excluída.", "sucesso")
    return redirect(url_for("routes.index"))
