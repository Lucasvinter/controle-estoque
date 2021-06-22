
from flask import Blueprint, request, jsonify

from app.domains.fornecedor.actions import create, get, get_fornecedor_by_id, alterar_fornecedor

app_fornecedor = Blueprint('app_fornecedor', __name__)


@app_fornecedor.route('/fornecedor', methods=['POST'])
def post():
    dados = request.get_json()
    print(dados)
    fornecedor = create(dados)
    return fornecedor.serialize(), 201

@app_fornecedor.route('/fornecedor', methods=['GET'])
def get_fornecedor():
    return jsonify([fornecedor.serialize() for fornecedor in get()]), 200

@app_fornecedor.route('/fornecedor/<id>', methods=['GET'])
def get_fornecedor_id(id):
    produto = get_fornecedor_by_id(id)
    return jsonify(produto.serialize()), 200

@app_fornecedor.route('/fornecedor/<id>', methods=['PUT'])
def put(id):
    dados = request.get_json()
    fornecedor = alterar_fornecedor(id, dados)
    return fornecedor.serialize(), 200