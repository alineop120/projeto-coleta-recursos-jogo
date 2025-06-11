import random
import threading
from core.mapa.map_utils import is_cell_walkable

# Semáforo para exclusão mútua entre threads dos NPCs
npc_lock = threading.Lock()

# Estado dos NPCs (posição no mapa)
npcs = {
    "npc1": {"x": 2, "y": 2},
    "npc2": {"x": 4, "y": 3},
}

direcoes = [
    (0, -1),  # cima
    (1, 0),   # direita
    (0, 1),   # baixo
    (-1, 0),  # esquerda
]

def mover_npc(nome):
    """Tenta mover o NPC para uma direção válida"""
    with npc_lock:
        npc = npcs.get(nome)
        if not npc:
            return

        dx, dy = random.choice(direcoes)
        novo_x = npc["x"] + dx
        novo_y = npc["y"] + dy

        if is_cell_walkable(novo_x, novo_y):
            npc["x"] = novo_x
            npc["y"] = novo_y
            print(f"{nome} se moveu para ({novo_x}, {novo_y})")

def atualizar_npcs():
    """Chamada periódica para mover todos os NPCs"""
    for nome in npcs:
        mover_npc(nome)

def get_npcs():
    """Retorna posição dos NPCs no formato pronto pro frontend"""
    with npc_lock:
        return {
            nome: {
                "posicao": {
                    "x": npc["x"] * 40,
                    "y": npc["y"] * 40,
                },
                "gridX": npc["x"],
                "gridY": npc["y"],
            }
            for nome, npc in npcs.items()
        }
