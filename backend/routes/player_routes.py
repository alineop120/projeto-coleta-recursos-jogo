from flask import Blueprint, request, jsonify
from core.players.player_manager import get_player
from core.players.player_service import mover_player, coletar_recurso
from core.recursos.recurso_manager import get_recursos

player_bp = Blueprint("player", __name__)

@player_bp.route("/estado", methods=["GET"])
def status():
    return jsonify(get_player())

@player_bp.route("/mover", methods=["POST"])
def mover():
    data = request.get_json()
    x, y = data.get("x"), data.get("y")
    if x is None or y is None:
        return jsonify({"ok": False, "mensagem": "Parâmetros inválidos."}), 400

    resultado = mover_player(x, y)
    return jsonify(resultado)

@player_bp.route("/coletar", methods=["POST"])
def coletar():
    data = request.get_json()
    x, y = data.get("x"), data.get("y")
    if x is None or y is None:
        return jsonify({"ok": False, "mensagem": "Parâmetros inválidos."}), 400

    recursos = get_recursos()
    resultado = coletar_recurso(x, y, recursos)
    return jsonify(resultado)
