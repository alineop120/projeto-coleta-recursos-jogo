# backend/core/recursos/recurso_threads.py
import threading
import time
from core.recursos.recurso_manager import gerar_recurso

def recurso_loop():
    while True:
        gerar_recurso()
        time.sleep(5)  # Gera um novo recurso a cada 5 segundos

def iniciar_thread_recursos():
    thread = threading.Thread(target=recurso_loop, daemon=True)
    thread.start()