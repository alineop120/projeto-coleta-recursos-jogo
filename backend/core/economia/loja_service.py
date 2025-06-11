# backend/core/economia/loja_service.py
import threading
from core.players.player_manager import get_jogador_por_id

loja_lock = threading.Semaphore(1)

itens_disponiveis = {
    "espada": 30,
    "mochila": 20,
    "poção": 15
}

def comprar_item(jogador_id, item):
    with loja_lock:
        jogador = get_jogador_por_id(jogador_id)

        if item not in itens_disponiveis:
            return {"sucesso": False, "mensagem": "Item inválido."}

        preco = itens_disponiveis[item]
        if jogador["moedas"] < preco:
            return {"sucesso": False, "mensagem": "Moedas insuficientes."}

        jogador["moedas"] -= preco
        jogador["inventario"].append(item)

        return {
            "sucesso": True,
            "mensagem": f"{item.capitalize()} comprado com sucesso!",
            "moedas": jogador["moedas"]
        }