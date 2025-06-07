# 🎮 Jogo de Coleta de Recursos com Threads

Jogo simples com NPCs controlados por threads no backend Python e frontend em React.

## 📌 Objetivo

Este projeto tem como foco criar um jogo onde o jogador coleta recursos, interage com NPCs e enfrenta inimigos, que são controlados por threads no backend para movimentação e ações concorrentes.

## 🗺️ Estrutura do Projeto
```bash
projeto-coleta-recursos-jogo/
│
├── backend/
│ ├── __pycache__
│ ├── .venv
│ ├── app.py # Servidor Flask e lógica backend
│ ├── npc.py # Threads e controle dos NPCs
│ ├── models.py
│ ├── services.py
│ ├── utils.py
│ └── requirements.txt
│
├── frontend/
│ ├── public/
│ ├── src/
│ │ ├── components/
│ │ │ ├── GameMap/
│ │ │ ├── NPCs/
│ │ │ │ ├── NPCs.jsx
│ │ │ │ └── NPCManager.js
│ │ │ ├── Player/
│ │ │ │ ├── Player.jsx
│ │ │ │ └── PlayerMovement.js
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