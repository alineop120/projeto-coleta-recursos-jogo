class Jogador:
    def __init__(self, nome="Herói"):
        self.nome = nome
        self.vida = 100
        self.moedas = 0
        self.recursos = 0
        self.mochila = 5
        self.espada = False
        self.posicao = {"x": 0, "y": 0}

    def to_dict(self):
        return {
            "nome": self.nome,
            "vida": self.vida,
            "moedas": self.moedas,
            "recursos": self.recursos,
            "mochila": self.mochila,
            "espada": self.espada,
            "posicao": self.posicao
        }


class NPCModel:
    def __init__(self, nome, x=0, y=0):
        self.nome = nome
        self.ativo = True
        self.posicao = {"x": x, "y": y}

    def to_dict(self):
        return {
            "ativo": self.ativo,
            "posicao": self.posicao
        }
