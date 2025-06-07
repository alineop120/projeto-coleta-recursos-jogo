import threading
import random
import time

class NPC(threading.Thread):
    def __init__(self, nome, estado_jogo, campo_lock, max_x=400, max_y=400, step=40):
        super().__init__(daemon=True)
        self.nome = nome
        self.estado_jogo = estado_jogo
        self.campo_lock = campo_lock
        self.max_x = max_x
        self.max_y = max_y
        self.step = step
        self.ativo = True

        with self.campo_lock:
            if nome not in self.estado_jogo:
                self.estado_jogo[nome] = {"ativo": True, "posicao": {"x": 0, "y": 0}}

    def run(self):
        while self.ativo and self.estado_jogo[self.nome]["ativo"]:
            with self.campo_lock:
                pos = self.estado_jogo[self.nome]["posicao"]
                novo_x = min(max(pos["x"] + random.choice([-self.step, 0, self.step]), 0), self.max_x)
                novo_y = min(max(pos["y"] + random.choice([-self.step, 0, self.step]), 0), self.max_y)

                self.estado_jogo[self.nome]["posicao"] = {"x": novo_x, "y": novo_y}
                print(f"{self.nome} se moveu para ({novo_x}, {novo_y})")

            time.sleep(1)

    def parar(self):
        self.ativo = False

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