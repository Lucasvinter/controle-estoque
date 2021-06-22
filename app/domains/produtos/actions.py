from app.domains.produtos.models import Produto
from database.repository import save, commit
from uuid import uuid4


def criar_produtos(dados):
    return save(Produto(id=str(uuid4()), name=dados['name'], codigo=dados['codigo']))


def get():
    return Produto.query.all()


def get_produto_by_id(id):
    return Produto.query.get(id)


def alterar_produto(id, dados):
    produto = get_produto_by_id(id)
    produto.name = dados.get('name')
    produto.codigo = dados.get('codigo')
    commit()
    return produto