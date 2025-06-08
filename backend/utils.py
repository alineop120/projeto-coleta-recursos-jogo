def validar_posicao(x, y, max_x=400, max_y=400, step=40):
    """Garante que a posição esteja dentro dos limites do mapa e alinhada à grade"""
    if x % step != 0 or y % step != 0:
        return False
    return 0 <= x <= max_x and 0 <= y <= max_y


def posicao_ocupada(estado_jogo, x, y, ignorar_nome=None):
    """Verifica se uma posição está ocupada por algum NPC"""
    for nome, entidade in estado_jogo.items():
        if nome == ignorar_nome:
            continue
        if isinstance(entidade, dict) and "posicao" in entidade:
            if entidade["posicao"]["x"] == x and entidade["posicao"]["y"] == y:
                return True
    return False
