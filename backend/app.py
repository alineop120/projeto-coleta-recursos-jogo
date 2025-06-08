from flask import Flask
from flask_cors import CORS

from routes.player import player_routes, obter_estado_e_lock
from routes.npc import npc_routes, configurar_npcs, NPCManager

from services import adicionar_recurso_periodicamente

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Registra as blueprints
app.register_blueprint(player_routes, url_prefix='/player')
app.register_blueprint(npc_routes, url_prefix='/npc')

# Obter estado e lock do módulo do jogador
estado_jogo, campo_lock = obter_estado_e_lock()

# Injetar estado nos NPCs
configurar_npcs(estado_jogo)

# Iniciar NPCs
npc_manager = NPCManager(estado_jogo, campo_lock)
npc_manager.start()

# supondo que estado_jogo já esteja criado
adicionar_recurso_periodicamente(estado_jogo)

if __name__ == '__main__':
    app.run(debug=True, port=5000)