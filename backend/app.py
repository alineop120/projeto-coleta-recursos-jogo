from flask import Flask
from flask_cors import CORS
from routes.player import player_routes

app = Flask(__name__)
CORS(app)

# Registrar as rotas do jogador
app.register_blueprint(player_routes)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
