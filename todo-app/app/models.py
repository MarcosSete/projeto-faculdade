"""
MODEL (camada de dados)
Representa a entidade "Tarefa" do banco de dados.
Corresponde à classe UML "Tarefa" do diagrama de classes do projeto
(ver docs/diagrama_de_classes.md).
"""
from datetime import datetime
from . import db


class Tarefa(db.Model):
    __tablename__ = "tarefa"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    descricao = db.Column(db.String(500), nullable=True)
    status = db.Column(db.String(20), nullable=False, default="Pendente")
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    data_vencimento = db.Column(db.Date, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "status": self.status,
            "data_criacao": self.data_criacao.strftime("%d/%m/%Y %H:%M") if self.data_criacao else None,
            "data_vencimento": self.data_vencimento.strftime("%d/%m/%Y") if self.data_vencimento else None,
        }

    def __repr__(self):
        return f"<Tarefa {self.id} - {self.titulo} - {self.status}>"
