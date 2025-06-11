import threading
import time
from backend.core.enemies.enemy_manager import atualizar_inimigos

def loop_inimigos():
    while True:
        atualizar_inimigos()
        time.sleep(4)  # Movimentação a cada 4 segundos

def iniciar_thread_inimigos():
    thread = threading.Thread(target=loop_inimigos, daemon=True)
    thread.start()
