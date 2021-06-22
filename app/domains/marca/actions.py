from uuid import uuid4

from app.domains.marca.models import Marca
from database.repository import save, commit


def create(dados):
    return save(Marca(id=str(uuid4()), nome=dados['nome'], id_fornecedor=dados['id_fornecedor']))


def get():
    return Marca.query.all()


def get_marca_by_id(id):
    return Marca.query.get(id)


def alterar_marca(id, dados):
    marca = get_marca_by_id(id)
    marca.nome = dados.get('nome')
    marca.id_fornecedor = dados.get('id_fornecedor')
    commit()
    return marca