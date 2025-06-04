import threading
import random
import time
from flask import Flask, request, jsonify
from flask_cors import CORS

# Estado do jogo
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
    "npc2": {"ativo": True, "posicao": {"x": 40, "y": 40}},  # inicialize as posições
    "campo": 0
}

campo_lock = threading.Lock()

from npc import NPCManager
npc_manager = NPCManager(estado_jogo, campo_lock)
npc_manager.start()

app = Flask(__name__)
CORS(app)

@app.route('/status', methods=['GET'])
def status_jogador():
    with campo_lock:
        return jsonify(estado_jogo["jogador"])

@app.route("/estado", methods=["GET"])
def obter_estado():
    return jsonify(estado_jogo)

@app.route("/coletar", methods=["POST"])
def coletar():
    with campo_lock:
        if estado_jogo["campo"] > 0:
            estado_jogo["campo"] -= 1
            estado_jogo["jogador"]["recursos"] += 1
    return jsonify(estado_jogo)

@app.route("/trocar", methods=["POST"])
def trocar():
    recursos = estado_jogo["jogador"]["recursos"]
    if recursos > 0:
        estado_jogo["jogador"]["moedas"] += recursos
        estado_jogo["jogador"]["recursos"] = 0
    return jsonify(estado_jogo)

@app.route("/comprar", methods=["POST"])
def comprar():
    item = request.json.get("item")
    custo = {"espada": 5, "mochila": 3}
    if item in custo and estado_jogo["jogador"]["moedas"] >= custo[item]:
        estado_jogo["jogador"]["moedas"] -= custo[item]
        if item == "espada":
            estado_jogo["jogador"]["espada"] = True
        elif item == "mochila":
            estado_jogo["jogador"]["mochila"] += 5
    return jsonify(estado_jogo)

@app.route('/mover', methods=['POST'])
def mover():
    dados = request.json
    x = dados.get('x')
    y = dados.get('y')
    if x is None or y is None:
        return jsonify({"erro": "Posição inválida"}), 400

    with campo_lock:
        estado_jogo["jogador"]["posicao"]["x"] = x
        estado_jogo["jogador"]["posicao"]["y"] = y

    return jsonify({"mensagem": "Posição atualizada", "posicao": estado_jogo["jogador"]["posicao"]})

if __name__ == '__main__':
    app.run(debug=True, port=5000)