import random
import threading
from core.mapa.map_utils import is_cell_walkable
from core.recursos.recurso_manager import gerar_recurso

inimigo_lock = threading.Lock()

inimigos = {
    "inimigo1": {"x": 2, "y": 2, "vida": 3},
    "inimigo2": {"x": 6, "y": 7, "vida": 3},
}

def mover_inimigo(nome):
    direcoes = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    dx, dy = random.choice(direcoes)

    with inimigo_lock:
        atual = inimigos[nome]
        novo_x = atual["x"] + dx
        novo_y = atual["y"] + dy

        if is_cell_walkable(novo_x, novo_y):
            atual["x"] = novo_x
            atual["y"] = novo_y
            print(f"{nome} se moveu para ({novo_x}, {novo_y})")

    if random.random() < 0.2:
        gerar_recurso(atual["x"], atual["y"])

def atualizar_inimigos():
    with inimigo_lock:
        for nome in inimigos:
            mover_inimigo(nome)

def get_inimigos():
    with inimigo_lock:
        return {
            nome: {
                "x": dados["x"] * 40,
                "y": dados["y"] * 40,
                "vida": dados["vida"]
            }
            for nome, dados in inimigos.items()
        }

def verificar_colisao_com_jogador(jogador_pos):
    jogador_grid = (jogador_pos["x"] // 40, jogador_pos["y"] // 40)
    with inimigo_lock:
        for nome, inimigo in inimigos.items():
            if (inimigo["x"], inimigo["y"]) == jogador_grid:
                print(f"{nome} atacou o jogador!")
                return True
    return False

def atacar_jogador(jogador):
    jogador["vida"] -= 1
    gerar_recurso(jogador["x"], jogador["y"])
    print(f"Jogador atacado! Vida restante: {jogador['vida']}")