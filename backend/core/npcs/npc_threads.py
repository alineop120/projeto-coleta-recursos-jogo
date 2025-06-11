import threading
import time
from core.npcs.npc_manager import atualizar_npcs

def npc_thread_loop():
    """Thread que move os NPCs a cada X segundos"""
    while True:
        atualizar_npcs()
        time.sleep(2)  # Delay entre movimentações (2s)

def iniciar_threads_npc():
    """Inicializa a thread de movimentação de NPCs"""
    thread = threading.Thread(target=npc_thread_loop, daemon=True)
    thread.start()
