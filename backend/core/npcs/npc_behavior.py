import random
import threading
import time
from core.players.player_manager import get_jogador_por_id
from core.economia.loja_service import comprar_item
from core.economia.guilda_service import trocar_recursos_por_moedas

class NPCThread(threading.Thread):
    def __init__(self, npc_id, nome):
        super().__init__()
        self.npc_id = npc_id
        self.nome = nome
        self.running = True
        self.daemon = True

    def run(self):
        while self.running:
            time.sleep(random.randint(5, 10))

            try:
                acao = random.choice(["comprar", "trocar"])
                jogador = get_jogador_por_id(self.npc_id)
                if not jogador:
                    print(f"{self.nome}: jogador não encontrado.")
                    continue

                if acao == "comprar":
                    item = random.choice(["espada", "mochila", "poção"])
                    resultado = comprar_item(self.npc_id, item)
                    print(f"{self.nome} tentou comprar {item}: {resultado['mensagem']}")
                else:
                    resultado = trocar_recursos_por_moedas(self.npc_id)
                    print(f"{self.nome} tentou trocar recursos: {resultado['mensagem']}")
            except Exception as e:
                print(f"Erro ao executar ação do NPC {self.nome}: {e}")

    def stop(self):
        self.running = False
