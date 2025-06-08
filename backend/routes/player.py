from flask import Blueprint, app, request, jsonify
from services import coletar_recurso, trocar_recursos, comprar_item
from utils import validar_posicao
from threading import Lock

# Blueprint de rotas do jogador
player_routes = Blueprint('player_routes', __name__)

# Estado do jogo e lock compartilhado
estado_jogo = {}
campo_lock = Lock()

def obter_estado_e_lock():
    return estado_jogo, campo_lock

# Função para configurar estado inicial do jogo
def configurar_jogo():
    global estado_jogo
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
        "npc1": {"ativo": True, "posicao": {"x": 0, "y": 0}, "recursos": 0},
        "npc2": {"ativo": True, "posicao": {"x": 40, "y": 40}, "recursos": 0},
        "recursos": [
            {"x": 120, "y": 160},
            {"x": 200, "y": 80},
            {"x": 80, "y": 240}
        ],
        "campo": 0,
    }
    return estado_jogo

# Inicia o estado do jogo
configurar_jogo()

# Rota: Obter status do jogador
@player_routes.route('/status', methods=['GET'])
def status_jogador():
    with campo_lock:
        return jsonify(estado_jogo["jogador"])


# Rota: Obter estado completo do jogo
@player_routes.route('/estado', methods=['GET'])
def obter_estado():
    return jsonify(estado_jogo)


# Rota: Coletar recurso
@player_routes.route('/coletar', methods=['POST'])
def coletar():
    print("Recebido no /coletar:", request.data)
    print("JSON recebido:", request.json)
    dados = request.json
    x = dados.get("x")
    y = dados.get("y")

    with campo_lock:
        coletar_recurso(estado_jogo, nome_entidade="jogador", x=x, y=y)

    return jsonify(estado_jogo)

# Rota: Trocar recurso por moedas
@player_routes.route('/trocar', methods=['POST'])
def trocar():
    with campo_lock:
        trocar_recursos(estado_jogo)
    return jsonify(estado_jogo)


# Rota: Comprar item
@player_routes.route('/comprar', methods=['POST'])
def comprar():
    item = request.json.get("item")
    with campo_lock:
        comprar_item(estado_jogo, item)
    return jsonify(estado_jogo)


# Rota: Mover jogador
@player_routes.route('/mover', methods=['POST'])
def mover():
    dados = request.json
    print("Dados recebidos no /mover:", dados)  # Adicione essa linha para debug

    x = dados.get('x')
    y = dados.get('y')

    if x is None or y is None or not validar_posicao(x, y):
        print("Validação falhou: x, y =", x, y)  # Debug
        return jsonify({"erro": "Posição inválida"}), 200

    with campo_lock:
        estado_jogo["jogador"]["posicao"] = {"x": x, "y": y}

    return jsonify({
        "mensagem": "Posição atualizada",
        "posicao": estado_jogo["jogador"]["posicao"]
    })

# Exporta para uso em outras rotas
def obter_estado_e_lock():
    return estado_jogo, campo_lock