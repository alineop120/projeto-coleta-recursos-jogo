from flask import Blueprint, jsonify
from backend.core.enemies.enemy_manager import get_inimigos

inimigo_bp = Blueprint("inimigo", __name__)

@inimigo_bp.route("/inimigos", methods=["GET"])
def listar_inimigos():
    return jsonify(get_inimigos())