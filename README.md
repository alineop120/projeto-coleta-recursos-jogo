# 🎮 Jogo de Coleta de Recursos com Threads

Um jogo multiplayer simples com NPCs inteligentes e movimentação concorrente usando Python, Flask e React.

![Status do Projeto](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.x-lightgrey)
![React](https://img.shields.io/badge/React-18.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)

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

### 🖼️ Galeria

![Tela inicial](./screenshots/main-menu.png)
*Menu principal com opções de jogo*

![Combate](./screenshots/battle.png)
*Sistema de turnos simplificado*

![Loja](./screenshots/shop.png)
*Interface de comércio com NPCs*

## 🗺️ Estrutura do Projeto
```yaml
projeto-coleta-recursos-jogo/
│
├── backend/
│ ├── core/
│ │ ├── economia/
│ │ │ ├── guilda_service.py
│ │ │ └── loja_service.py
│ │ ├── enemies/
│ │ │ ├── enemy_manager.py
│ │ │ └── enemy_threads.py
│ │ ├── mapa/
│ │ │ ├── map_data.py
│ │ │ └── map_utils.py
│ │ ├── npcs/
│ │ │ ├── npc_behavior.py
│ │ │ ├── npc_manager.py
│ │ │ └── npc_threads.py
│ │ ├── players/
│ │ │ ├── player_manager.py
│ │ │ └── player_threads.py
│ │ └── recursos/
│ │ │ ├── recurso_manager.py
│ │ │ └── recurso_threads.py
│ ├── routes/
│ │ ├── enemy_routes.py
│ │ ├── loja_guilda_routes.py
│ │ ├── npc_routes.py
│ │ ├── player_routes.py
│ │ └── recurso_routes.py
│ ├── services/
│ │ └── socket_service.py
│ ├── tests/
│ │ ├── test_npc_routes.py
│ │ └── test_player_routes.py
│ ├── app.py
│ └── requirements.txt
│
├── frontend/
│ ├── public/
│ ├── src/
│ │ ├── components/
│ │ │ ├── GameMap/
│ │ │ │ ├── GameMap.css
│ │ │ │ ├── GameMap.jsx
│ │ │ │ └── mapaUtils.js
│ │ │ ├── LojaGuilda/
│ │ │ │ ├── Guilda.jsx
│ │ │ │ └── Loja.jsx
│ │ │ ├── NPCs/
│ │ │ │ ├── NPCsList.jsx
│ │ │ │ └── NPCStatus.js
│ │ │ ├── Player/
│ │ │ │ ├── PlayerMovement.jsx
│ │ │ │ └── PlayerStatus.jsx
│ │ │ ├── Resources/
│ │ │ │ └── Resources.jsx
│ │ │ ├── UI/
│ │ │ │ └── Modal.jsx
│ │ ├── context/
│ │ │ └── gameContext.jsx
│ │ ├── hooks/
│ │ │ └── useGameLogic.js
│ │ ├── services/
│ │ │ └── api.jsx
│ │ ├── styles/
│ │ │ └── variables.css
│ │ ├── App.jsx
│ │ └── index.js
│ ├── .babelrc
│ ├── package-lock.json
│ ├── package.json
│ └── webpack.config.js
│
├── .gitattributes
├── .gitignore
└── README.md # Este arquivo
```

## 🕹️ Funcionalidades Detalhadas

### Jogador Principal
- Movimentação em 4 direções (WASD ou setas)
- Sistema de inventário com capacidade limitada
- Barra de saúde e atributos (fome, resistência)
- Habilidades especiais com cooldown

### NPCs Inteligentes
- Rotinas diárias simuladas (coleta, comércio, descanso)
- Comportamentos reativos a eventos do jogo
- Sistema de prioridades para tomada de decisão
- Personalidades distintas (agressivo, pacífico, comerciante)

### Sistema Econômico
- Flutuação de preços baseada em oferta/demanda
- Diferentes guildas com especialidades únicas
- Upgrades progressivos para equipamentos
- Sistema de leilão para itens raros

### Combate
- Inimigos com padrões de ataque distintos
- Sistema de vantagens/desvantagens por tipo
- Drops aleatórios com tabelas de loot
- Chefes periódicos com mecânicas especiais

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

```
- O backend roda em http://localhost:5000 e o frontend em http://localhost:3000.

## 🛠️ Desafios Técnicos e Soluções

| Desafio | Solução Implementada | Código Exemplo |
|---------|----------------------|----------------|
| Race conditions nos recursos | Semáforos binários | `threading.Semaphore(1)` |
| Atualização inconsistente do estado | Padrão Observer | `Publisher-Subscriber` |
| Deadlocks em interações complexas | Timeout em aquisição de locks | `lock.acquire(timeout=5)` |
| Latência na comunicação | Cache local no frontend | `useMemo` no React |
| Pathfinding de NPCs | Algoritmo A* simplificado | `priority_queue` em Python |

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

> 📌 Para qualquer dúvida ou sugestão, [abra uma issue aqui](https://github.com/alineop120/projeto-coleta-recursos-jogo/issues).

---

>**⌨️ com ❤️ por [Aline](https://github.com/alineop120), [Ana Beatriz](https://github.com/Anabamorim) & [Camila](https://github.com/)**  
_Projeto acadêmico desenvolvido para a disciplina de Sistemas Operacionais - 2025_