"""
CONTROLLER (camada de controle)
Recebe as requisições HTTP, fala com o Model (Tarefa) e decide
qual View (template) devolver para o usuário.
"""
from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db
from .models import Tarefa

bp = Blueprint("routes", __name__)


def _parse_data(valor):
    if not valor:
        return None
    return datetime.strptime(valor, "%Y-%m-%d").date()


@bp.route("/")
def index():
    """Lista todas as tarefas (Read)."""
    tarefas = Tarefa.query.order_by(Tarefa.data_criacao.desc()).all()
    return render_template("index.html", tarefas=tarefas)


@bp.route("/nova", methods=["GET", "POST"])
def nova_tarefa():
    """Cria uma nova tarefa (Create)."""
    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        if not titulo:
            flash("O título é obrigatório.", "erro")
            return render_template("form.html", tarefa=None)

        tarefa = Tarefa(
            titulo=titulo,
            descricao=request.form.get("descricao", "").strip(),
            data_vencimento=_parse_data(request.form.get("data_vencimento")),
        )
        db.session.add(tarefa)
        db.session.commit()
        flash("Tarefa criada com sucesso!", "sucesso")
        return redirect(url_for("routes.index"))

    return render_template("form.html", tarefa=None)


@bp.route("/editar/<int:tarefa_id>", methods=["GET", "POST"])
def editar_tarefa(tarefa_id):
    """Edita uma tarefa existente (Update)."""
    tarefa = Tarefa.query.get_or_404(tarefa_id)

    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        if not titulo:
            flash("O título é obrigatório.", "erro")
            return render_template("form.html", tarefa=tarefa)

        tarefa.titulo = titulo
        tarefa.descricao = request.form.get("descricao", "").strip()
        tarefa.status = request.form.get("status", tarefa.status)
        tarefa.data_vencimento = _parse_data(request.form.get("data_vencimento"))
        db.session.commit()
        flash("Tarefa atualizada com sucesso!", "sucesso")
        return redirect(url_for("routes.index"))

    return render_template("form.html", tarefa=tarefa)


@bp.route("/concluir/<int:tarefa_id>", methods=["POST"])
def concluir_tarefa(tarefa_id):
    """Alterna o status entre Pendente e Concluída."""
    tarefa = Tarefa.query.get_or_404(tarefa_id)
    tarefa.status = "Concluída" if tarefa.status != "Concluída" else "Pendente"
    db.session.commit()
    return redirect(url_for("routes.index"))


@bp.route("/excluir/<int:tarefa_id>", methods=["POST"])
def excluir_tarefa(tarefa_id):
    """Remove uma tarefa (Delete)."""
    tarefa = Tarefa.query.get_or_404(tarefa_id)
    db.session.delete(tarefa)
    db.session.commit()
    flash("Tarefa excluída.", "sucesso")
    return redirect(url_for("routes.index"))
