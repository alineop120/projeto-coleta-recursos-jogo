from flask import Blueprint, jsonify
import threading
import random
import time

npc_routes = Blueprint("npc_routes", __name__)

# Estado e lock globais compartilhados (serão substituídos por injeção futura)
estado_jogo = {}
campo_lock = threading.Lock()


class NPC(threading.Thread):
    def __init__(self, nome, estado_jogo, campo_lock, max_x=400, max_y=400, step=40):
        super().__init__(daemon=True)
        self.nome = nome
        self.estado_jogo = estado_jogo
        self.campo_lock = campo_lock
        self.max_x = max_x
        self.max_y = max_y
        self.step = step
        self._stop_event = threading.Event()

        with self.campo_lock:
            if nome not in self.estado_jogo:
                self.estado_jogo[nome] = {"ativo": True, "posicao": {"x": 0, "y": 0}}

    def run(self):
        while not self._stop_event.is_set():
            with self.campo_lock:
                pos = self.estado_jogo[self.nome]["posicao"]
                novo_x = min(max(pos["x"] + random.choice([-self.step, 0, self.step]), 0), self.max_x)
                novo_y = min(max(pos["y"] + random.choice([-self.step, 0, self.step]), 0), self.max_y)
                self.estado_jogo[self.nome]["posicao"] = {"x": novo_x, "y": novo_y}
                print(f"{self.nome} se moveu para ({novo_x}, {novo_y})")
            time.sleep(1)

    def parar(self):
        self._stop_event.set()


class NPCManager:
    def __init__(self, estado_jogo, campo_lock):
        self.estado_jogo = estado_jogo
        self.campo_lock = campo_lock
        self.npcs = []

        for nome in ["npc1", "npc2"]:
            npc = NPC(nome, estado_jogo, campo_lock)
            self.npcs.append(npc)

    def start(self):
        for npc in self.npcs:
            npc.start()

    def stop(self):
        for npc in self.npcs:
            npc.parar()


# Função para injetar o estado do jogo
def configurar_npcs(estado):
    global estado_jogo
    estado_jogo = estado


# Exemplo de rota para ver posição dos NPCs
@npc_routes.route('/npcs', methods=['GET'])
def listar_npcs():
    with campo_lock:
        npcs = {k: v for k, v in estado_jogo.items() if k.startswith("npc")}
        return jsonify(npcs)
