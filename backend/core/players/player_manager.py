import threading

player_lock = threading.Lock()

# Estado inicial do jogador
jogador = {
    "nome": "Heroi",
    "x": 0,
    "y": 0,
    "vida": 5,
    "moedas": 0,
    "recursos": 0,
    "mochila": [],
}

def get_jogador_por_id():
    # Como só há um jogador, ignora o ID
    return get_player_raw()

def get_player():
    with player_lock:
        return {
            "nome": jogador["nome"],
            "x": jogador["x"] * 40,
            "y": jogador["y"] * 40,
            "vida": jogador["vida"],
            "moedas": jogador["moedas"],
            "recursos": jogador["recursos"],
            "mochila": jogador["mochila"],
        }

def get_player_raw():
    """Retorna o jogador com coordenadas em grid (não multiplicadas por 40)."""
    with player_lock:
        return dict(jogador)

def atualizar_player(data):
    with player_lock:
        jogador.update(data)