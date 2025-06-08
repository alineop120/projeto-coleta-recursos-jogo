def coletar_recurso(estado_jogo):
    if estado_jogo["campo"] > 0:
        estado_jogo["campo"] -= 1
        estado_jogo["jogador"]["recursos"] += 1
    return estado_jogo


def trocar_recursos(estado_jogo):
    recursos = estado_jogo["jogador"]["recursos"]
    if recursos > 0:
        estado_jogo["jogador"]["moedas"] += recursos
        estado_jogo["jogador"]["recursos"] = 0
    return estado_jogo


def comprar_item(estado_jogo, item):
    custo = {"espada": 5, "mochila": 3}
    jogador = estado_jogo["jogador"]

    if item in custo and jogador["moedas"] >= custo[item]:
        jogador["moedas"] -= custo[item]
        if item == "espada":
            jogador["espada"] = True
        elif item == "mochila":
            jogador["mochila"] += 5
    return estado_jogo
