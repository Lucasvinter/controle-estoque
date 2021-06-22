from uuid import uuid4

from app.domains.fornecedor.models import Fornecedor
from database.repository import save, commit


def create(dados):
    return save(Fornecedor(id=str(uuid4()), nome=dados['nome'], cnpj=dados['cnpj']))


def get():
    return Fornecedor.query.all()


def get_fornecedor_by_id(id):
    return Fornecedor.query.get(id)


def alterar_fornecedor(id, dados):
    fornecedor = get_fornecedor_by_id(id)
    fornecedor.nome = dados.get('nome')
    fornecedor.cnpj = dados.get('cnpj')
    commit()
    return fornecedor
