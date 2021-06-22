from database import db


class Produto(db.Model):
    __tablename__ = 'produto'

    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(80))
    codigo = db.Column(db.String(255))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'codigo': self.codigo,
        }