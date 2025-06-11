from flask import Blueprint, jsonify
from core.npcs.npc_manager import get_npcs

npc_bp = Blueprint("npc", __name__)

@npc_bp.route("/estado", methods=["GET"])
def estado_npcs():
    return jsonify(get_npcs())
