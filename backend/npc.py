import threading
import random
import time

class NPCManager:
    def __init__(self, estado_jogo, campo_lock):
        self.estado_jogo = estado_jogo
        self.campo_lock = campo_lock
        self.npcs = ["npc1", "npc2"]
        self.threads = []

        for npc in self.npcs:
            if npc not in self.estado_jogo:
                self.estado_jogo[npc] = {"ativo": True, "posicao": {"x": 0, "y": 0}}

    def start(self):
        for npc in self.npcs:
            t = threading.Thread(target=self.mover_npc, args=(npc,), daemon=True)  # ← AQUI FOI CORRIGIDO
            t.start()
            self.threads.append(t)

    def mover_npc(self, nome):
        while self.estado_jogo[nome]["ativo"]:
            with self.campo_lock:
                pos = self.estado_jogo[nome]["posicao"]
                step = 40
                max_x = 400
                max_y = 400

                novo_x = min(max(pos["x"] + random.choice([-step, 0, step]), 0), max_x)
                novo_y = min(max(pos["y"] + random.choice([-step, 0, step]), 0), max_y)

                self.estado_jogo[nome]["posicao"] = {"x": novo_x, "y": novo_y}
                print(f"{nome} se moveu para ({novo_x}, {novo_y})")

            time.sleep(1)