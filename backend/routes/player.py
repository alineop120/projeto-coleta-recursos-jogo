from flask import Blueprint, request, jsonify

player_routes = Blueprint('player', __name__)

# Variáveis globais injetadas via configurar_jogo
estado_jogo = None
campo_lock = None

def configurar_jogo(estado, lock):
    global estado_jogo, campo_lock
    estado_jogo = estado
    campo_lock = lock

@player_routes.route('/status', methods=['GET'])
def status_jogador():
    with campo_lock:
        return jsonify(estado_jogo["jogador"])

@player_routes.route('/mover', methods=['POST'])
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

@player_routes.route('/coletar', methods=['POST'])
def coletar():
    with campo_lock:
        if estado_jogo["campo"] > 0:
            estado_jogo["campo"] -= 1
            estado_jogo["jogador"]["recursos"] += 1
            return jsonify({"mensagem": "Recurso coletado com sucesso", "estado": estado_jogo})
        else:
            return jsonify({"mensagem": "Nenhum recurso disponível"}), 400

@player_routes.route('/trocar', methods=['POST'])
def trocar():
    with campo_lock:
        recursos = estado_jogo["jogador"]["recursos"]
        if recursos > 0:
            estado_jogo["jogador"]["moedas"] += recursos
            estado_jogo["jogador"]["recursos"] = 0
            return jsonify({"mensagem": "Troca realizada com sucesso", "estado": estado_jogo})
        else:
            return jsonify({"mensagem": "Sem recursos para trocar"}), 400

@player_routes.route('/comprar', methods=['POST'])
def comprar():
    data = request.get_json()
    if not data or "item" not in data:
        return jsonify({"erro": "Requisição inválida"}), 400

    item = data["item"]
    custo = {"espada": 5, "mochila": 3}

    with campo_lock:
        if item in custo and estado_jogo["jogador"]["moedas"] >= custo[item]:
            estado_jogo["jogador"]["moedas"] -= custo[item]
            if item == "espada":
                estado_jogo["jogador"]["espada"] = True
            elif item == "mochila":
                estado_jogo["jogador"]["mochila"] += 5
            return jsonify({"mensagem": f"{item} comprado com sucesso", "estado": estado_jogo})
        else:
            return jsonify({"mensagem": "Moedas insuficientes ou item inválido"}), 400