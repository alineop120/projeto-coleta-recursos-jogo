import threading
from core.players.player_manager import get_jogador_por_id

guilda_lock = threading.Semaphore(1)

def trocar_recursos_por_moedas(jogador_id):
    with guilda_lock:
        jogador = get_jogador_por_id(jogador_id)

        if jogador["recursos"] == 0:
            return {"sucesso": False, "mensagem": "Você não tem recursos para trocar."}

        moedas_geradas = jogador["recursos"] * 5
        jogador["moedas"] += moedas_geradas
        jogador["recursos"] = 0

        return {
            "sucesso": True,
            "mensagem": f"Você trocou por {moedas_geradas} moedas.",
            "moedas": jogador["moedas"]
        }
