from database import db


class Marca(db.Model):
    __tablename__ = 'marca'

    id = db.Column(db.String(36), primary_key=True)
    nome = db.Column(db.String(80))
    id_fornecedor = db.Column(db.String(36), db.ForeignKey('fornecedor.id'))
    fornecedor = db.relationship('Fornecedor')

    def serialize(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'id_fornecedor': self.id_fornecedor,
        }

