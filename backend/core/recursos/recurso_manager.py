import random
import threading
from core.mapa.map_utils import is_cell_walkable

recurso_lock = threading.Lock()

# Lista de recursos no formato: {'x': 2, 'y': 5}
recursos = []

def gerar_recurso():
    """Gera um recurso em uma célula aleatória válida"""
    while True:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if is_cell_walkable(x, y):
            with recurso_lock:
                # Evita criar recurso onde já existe
                if not any(r["x"] == x and r["y"] == y for r in recursos):
                    recursos.append({"x": x, "y": y})
                    print(f"Recurso criado em ({x}, {y})")
                    break

def remover_recurso(x, y):
    """Remove recurso coletado"""
    with recurso_lock:
        global recursos
        recursos = [r for r in recursos if r["x"] != x or r["y"] != y]
        print(f"Recurso em ({x}, {y}) foi coletado")

def get_recursos():
    """Retorna os recursos formatados para o frontend"""
    with recurso_lock:
        return [{"x": r["x"] * 40, "y": r["y"] * 40} for r in recursos]

def existe_recurso_em(x, y):
    with recurso_lock:
        return any(r["x"] == x and r["y"] == y for r in recursos)
