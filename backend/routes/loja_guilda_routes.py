from flask import Blueprint, request, jsonify
from core.economia.loja_service import comprar_item
from core.economia.guilda_service import trocar_recursos_por_moedas

loja_guilda_bp = Blueprint("loja_guilda", __name__)

@loja_guilda_bp.route("/player/comprar", methods=["POST"])
def comprar():
    data = request.get_json()
    jogador_id = 1  # fixo por enquanto
    item = data.get("item")
    resultado = comprar_item(jogador_id, item)
    return jsonify(resultado)

@loja_guilda_bp.route("/player/trocar", methods=["POST"])
def trocar():
    jogador_id = 1  # fixo por enquanto
    resultado = trocar_recursos_por_moedas(jogador_id)
    return jsonify(resultado)
