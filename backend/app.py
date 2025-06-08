from flask import Flask, jsonify
from flask_cors import CORS
from npc import NPCManager
import threading

from routes.player import player_routes, configurar_jogo

# Estado compartilhado
estado_jogo = {
    "jogador": {
        "nome": "Herói",
        "vida": 100,
        "moedas": 0,
        "recursos": 0,
        "mochila": 5,
        "espada": False,
        "posicao": {"x": 0, "y": 0}
    },
    "npc1": {"ativo": True, "posicao": {"x": 0, "y": 0}},
    "npc2": {"ativo": True, "posicao": {"x": 40, "y": 40}},
    "campo": 0
}

campo_lock = threading.Lock()

# Iniciar NPCs
npc_manager = NPCManager(estado_jogo, campo_lock)
npc_manager.start()

# Configurar Flask
app = Flask(__name__)
CORS(app)

# Injetar dependências nas rotas
configurar_jogo(estado_jogo, campo_lock)
app.register_blueprint(player_routes)

@app.route("/estado", methods=["GET"])
def obter_estado():
    with campo_lock:
        return jsonify(estado_jogo)

if __name__ == '__main__':
    app.run(debug=True, port=5000)