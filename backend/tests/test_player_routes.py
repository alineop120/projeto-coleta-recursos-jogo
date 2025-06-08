import pytest
from flask import Flask
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from routes.player import player_routes, configurar_jogo

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(player_routes)

    estado_jogo = {
        "jogador": {
            "nome": "Herói",
            "vida": 100,
            "moedas": 10,
            "recursos": 2,
            "mochila": 5,
            "espada": False,
            "posicao": {"x": 0, "y": 0}
        },
        "campo": 3
    }
    from threading import Lock
    campo_lock = Lock()

    configurar_jogo(estado_jogo, campo_lock)
    app.config["estado_jogo"] = estado_jogo
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_status_jogador(client):
    response = client.get('/status')
    assert response.status_code == 200
    data = response.get_json()
    assert data["nome"] == "Herói"
    assert "vida" in data

def test_mover_jogador(client):
    response = client.post('/mover', json={"x": 80, "y": 40})
    assert response.status_code == 200
    data = response.get_json()
    assert data["posicao"]["x"] == 80
    assert data["posicao"]["y"] == 40

def test_coletar(client):
    response = client.post('/coletar')
    data = response.get_json()
    assert response.status_code == 200
    assert "estado" in data
    assert data["estado"]["jogador"]["recursos"] >= 1

def test_comprar_espada(client):
    response = client.post('/comprar', json={"item": "espada"})
    data = response.get_json()
    assert response.status_code == 200
    assert data["estado"]["jogador"]["espada"] is True