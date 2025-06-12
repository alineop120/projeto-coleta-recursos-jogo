# 🎮 Jogo de Coleta de Recursos com Threads

Um jogo multiplayer simples com NPCs inteligentes e movimentação concorrente usando Python, Flask e React.

## 📌 Objetivo

Este projeto tem como foco criar um jogo onde o jogador coleta recursos, interage com NPCs e enfrenta inimigos, que são controlados por threads no backend para movimentação e ações concorrentes.

## 🛠️ Tecnologias Utilizadas

- **Python 3.11**
- **Flask** – API e controle do jogo
- **ReactJS** – Frontend e interface
- **Threading e Semáforos** – Controle de concorrência no backend
- **Axios** – Requisições assíncronas no frontend

## 📸 Preview

![Demonstração do jogo](./assets/demo.gif)

## 🗺️ Estrutura do Projeto
```bash
projeto-coleta-recursos-jogo/
│
├── backend/
│ ├── routes/
│ │ ├── npc.py
│ │ └── player.py
│ ├── tests/
│ │ └── test_player_routes.py
│ ├── app.py
│ ├── models.py
│ ├── requirements.txt
│ ├── services.py
│ └── utils.py
│
├── frontend/
│ ├── public/
│ ├── src/
│ │ ├── components/
│ │ │ ├── Maps/
│ │ │ │ ├── Locations/
│ │ │ │ │ ├── Guilda.jsx
│ │ │ │ │ └── Loja.jsx
│ │ │ │ ├── GameMap.jsx
│ │ │ │ ├── mapaData.js
│ │ │ │ └── mapaUtils.js
│ │ │ ├── NPCs/
│ │ │ │ ├── NPCs.jsx
│ │ │ │ └── NPCManager.js
│ │ │ ├── Player/
│ │ │ │ ├── Player.jsx
│ │ │ │ └── PlayerMovement.js
│ │ │ ├── Resources/
│ │ │ │ └── Resources.jsx
│ │ ├── services/
│ │ │ └── api.jsx
│ │ ├── PlayerMovement.js
│ │ ├── App.jsx
│ │ └── index.js
│ └── package.json
│
├── .gitignore
└── README.md # Este arquivo
```

## 🕹️ Funcionalidades

- Movimentação do jogador via React
- NPCs e inimigos movimentados por threads no backend Python
- Mapa interativo com obstáculos, guildas e lojas
- Sincronização em tempo real via chamadas periódicas à API
- Controle de estado com locks para evitar conflitos no backend

## ⚙️ Concor­rência no Backend

O backend usa **threads** para simular NPCs e inimigos de forma independente, com atualizações periódicas a cada segundo. 

Para evitar condições de corrida, o projeto utiliza:

- `threading.Thread` para criar NPCs autônomos;
- `threading.Lock` para sincronizar acesso a recursos compartilhados;
- `threading.Semaphore` para controlar o número de NPCs em regiões limitadas do mapa.

Esse modelo garante que múltiplos NPCs possam atuar simultaneamente sem corromper o estado global do jogo.

## 🚀 Como rodar

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
python app.py
```

### Frontend
```bash
cd frontend
npm init -y
npm install
npm start
```
- O backend roda em http://localhost:5000 e o frontend em http://localhost:3000.

### 👥 Equipe

Projeto desenvolvido por:

| Nome                  | Função                     | GitHub                                       |
|-----------------------|----------------------------|----------------------------------------------|
| *Aline Oliveira*      | Desenvolvedora Back-end    | [@alineop120](https://github.com/alineop120) |
| *Ana Beatriz Amorim*  | Analista de Requisitos     | [@Anabamorim](https://github.com/Anabamorim) |
| *Camila Mendes*       | Desenvolvedora Front-end   | N/A                                          |

### 📋 Observações

- NPCs atualizam suas posições a cada segundo no backend, e os dados são enviados ao frontend.
- O mapa é dividido em células de 40x40px para facilitar movimentação e colisões.
- Use o componente NPCs.js para renderizar NPCs na tela.

### 🤝 Contato

> 📌 Para qualquer dúvida ou sugestão, [abra uma issue aqui](https://github.com/SEU_REPOSITORIO/issues).