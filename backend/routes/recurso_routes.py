from flask import Blueprint, jsonify, request
from core.recursos.recurso_manager import get_recursos, remover_recurso, existe_recurso_em

recurso_bp = Blueprint("recurso", __name__)

@recurso_bp.route("/recursos", methods=["GET"])
def listar_recursos():
    return jsonify(get_recursos())

@recurso_bp.route("/coletar", methods=["POST"])
def coletar():
    dados = request.get_json()
    x = dados.get("x") // 40  # converte de px para grid
    y = dados.get("y") // 40

    if existe_recurso_em(x, y):
        remover_recurso(x, y)
        return jsonify({"mensagem": "Recurso coletado com sucesso"}), 200
    else:
        return jsonify({"mensagem": "Nenhum recurso aqui"}), 404
