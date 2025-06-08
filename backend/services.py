from models.resources import recursos_no_mapa
from threading import Lock

recurso_lock = Lock()

def coletar_recurso(estado_jogo, nome_entidade, x=None, y=None):
    with recurso_lock:  # garante exclusividade na alteração
        entidade = estado_jogo[nome_entidade]
        pos = entidade["posicao"]

        alvo_x = x if x is not None else pos["x"]
        alvo_y = y if y is not None else pos["y"]

        for recurso in estado_jogo["recursos"]:
            if recurso["x"] == alvo_x and recurso["y"] == alvo_y:
                estado_jogo["recursos"].remove(recurso)
                if "recursos" not in entidade:
                    entidade["recursos"] = 0
                entidade["recursos"] += 1
                print(f"{nome_entidade} coletou recurso em ({alvo_x}, {alvo_y})")
                break

    return estado_jogo

def trocar_recursos(estado_jogo):
    with recurso_lock:
        recursos = estado_jogo["jogador"].get("recursos", 0)
        if recursos > 0:
            estado_jogo["jogador"]["moedas"] += recursos
            estado_jogo["jogador"]["recursos"] = 0
    return estado_jogo

def comprar_item(estado_jogo, item):
    custo = {"espada": 5, "mochila": 3}
    jogador = estado_jogo["jogador"]

    if item not in custo:
        return estado_jogo, False  # item inválido

    if jogador["moedas"] >= custo[item]:
        jogador["moedas"] -= custo[item]
        if item == "espada":
            jogador["espada"] = True
        elif item == "mochila":
            jogador["mochila"] += 5
        return estado_jogo, True

    return estado_jogo, False  # sem moedas suficientes
