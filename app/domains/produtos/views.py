from flask import Blueprint, request, jsonify

from app.domains.produtos.actions import get, criar_produtos, alterar_produto, get_produto_by_id

app_produtos = Blueprint('app_produtos', __name__)


@app_produtos.route('/produto', methods=['POST'])
def post():
    dados = request.get_json()
    produto = criar_produtos(dados)
    return produto.serialize(), 201


@app_produtos.route('/produto/<id>', methods=['PUT'])
def put(id):
    dados = request.get_json()
    produto = alterar_produto(id, dados)
    return produto.serialize(), 200


@app_produtos.route('/produto', methods=['GET'])
def get():
    return jsonify([produto.serialize() for produto in get()]), 200


@app_produtos.route('/produto/<id>', methods=['GET'])
def get_by_id(id):
    produto = get_produto_by_id(id)
    return jsonify(produto.serialize()), 200