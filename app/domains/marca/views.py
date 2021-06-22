from flask import Blueprint, request, jsonify

from app.domains.marca.actions import create, get_marca_by_id, alterar_marca, get

app_marca = Blueprint('app_marca', __name__)

@app_marca.route('/marca', methods=['POST'])
def post():
    dados = request.get_json()
    marca = create(dados)
    return marca.serialize(), 201



@app_marca.route('/marca/<id>', methods=['PUT'])
def put(id):
    dados = request.get_json()
    marca = alterar_marca(id, dados)
    return marca.serialize(), 200


@app_marca.route('/marca', methods=['GET'])
def get_marca():
    return jsonify([marca.serialize() for marca in get()]), 200


@app_marca.route('/marca/<id>', methods=['GET'])
def get_by_id(id):
    marca = get_marca_by_id(id)
    return jsonify(marca.serialize()), 200