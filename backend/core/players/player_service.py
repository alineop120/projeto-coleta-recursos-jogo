# backend/core/player/player_service.py
from core.players.player_manager import jogador, player_lock
from core.mapa.map_utils import is_cell_walkable
from core.enemies.enemy_manager import verificar_colisao_com_jogador

def mover_player(novo_x, novo_y):
    grid_x = novo_x // 40
    grid_y = novo_y // 40

    if not is_cell_walkable(grid_x, grid_y):
        return {"ok": False, "mensagem": "Movimento inválido!"}

    with player_lock:
        jogador["x"] = grid_x
        jogador["y"] = grid_y

        # Checa colisão com inimigos
        if verificar_colisao_com_jogador({"x": novo_x, "y": novo_y}):
            jogador["vida"] -= 1
            return {"ok": True, "mensagem": "Você foi atacado por um inimigo!"}

    return {"ok": True, "mensagem": "Movido com sucesso."}

def coletar_recurso(x, y, recursos):
    grid_x = x // 40
    grid_y = y // 40

    with player_lock:
        for recurso in recursos:
            if recurso["x"] == grid_x and recurso["y"] == grid_y:
                jogador["recursos"] += 1
                jogador["mochila"].append("recurso")
                return {"ok": True, "mensagem": "Recurso coletado!"}
    return {"ok": False, "mensagem": "Nenhum recurso nesta posição."}