from database import db


class Fornecedor(db.Model):
    __tablename__ = 'fornecedor'

    id = db.Column(db.String(36), primary_key=True)
    nome = db.Column(db.String(80))
    cnpj = db.Column(db.Integer())

    def serialize(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cnpj': self.cnpj,
        }