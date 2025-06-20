from flask import Flask
from flask_cors import CORS
import threading

from routes.player_routes import player_bp
from routes.npc_routes import npc_bp

from routes.npc_routes import npc_bp
from core.npcs.npc_threads import iniciar_threads_npc

from routes.recurso_routes import recurso_bp
from core.recursos.recurso_threads import iniciar_thread_recursos

from routes.loja_guilda_routes import loja_guilda_bp

app = Flask(__name__)
CORS(app)

# Registrando Blueprints (rotas)
app.register_blueprint(player_bp)
app.register_blueprint(npc_bp)
app.register_blueprint(recurso_bp)
app.register_blueprint(loja_guilda_bp)

# Inicia threads de NPCs
threading.Thread(target=iniciar_threads_npc, daemon=True).start()

# Inicia thread de recursos
threading.Thread(target=iniciar_thread_recursos, daemon=True).start()

if __name__ == '__main__':
    app.run(debug=True)
