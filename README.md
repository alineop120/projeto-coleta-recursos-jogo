<h1 align="center">🎮 Jogo de Coleta de Recursos com Threads</h1>

<p align="center">
  Jogo simples com NPCs controlados por threads no backend Python e frontend em React.
</p>

<hr/>

<h2>📌 Objetivo</h2>
<p>Este projeto tem como foco criar um jogo onde o jogador coleta recursos, interage com NPCs e enfrenta inimigos, que são controlados por threads no backend para movimentação e ações concorrentes.</p>

<h2>🗺️ Estrutura do Projeto</h2>
<pre>
jogo-recursos-threads/
├── backend/
│   ├── app.py          # Servidor Flask e lógica backend
│   ├── npc.py          # Threads e controle dos NPCs
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── map/
│   │   │   ├── threads/
│   │   │   │   └── NPCs.js    # Componente para renderizar NPCs
│   │   └── PlayerMovement.js
│   │   ├── App.jsx
│   │   └── index.js
│   └── package.json
└── README.html         # Este arquivo
</pre>

<h2>🕹️ Funcionalidades</h2>
<ul>
  <li>Movimentação do jogador via React</li>
  <li>NPCs e inimigos movimentados por threads no backend Python</li>
  <li>Mapa interativo com obstáculos, guildas e lojas</li>
  <li>Sincronização em tempo real via chamadas periódicas à API</li>
  <li>Controle de estado com locks para evitar conflitos no backend</li>
</ul>

<h2>🚀 Como rodar</h2>

<h3>Backend</h3>
<pre><code>python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
pip install -r requirements.txt
python app.py
</code></pre>

<h3>Frontend</h3>
<pre><code>npm install
npm start
</code></pre>

<p>O backend roda em <code>http://localhost:5000</code> e o frontend em <code>http://localhost:3000</code>.</p>

<h2>🔧 Tecnologias</h2>
<ul>
  <li>Python 3, Flask, threading</li>
  <li>React, Axios</li>
</ul>

<h2>👥 Equipe</h2>
<div align="center">
  <p>Projeto desenvolvido por:</p>
  <table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse;">
    <thead>
      <tr style="background-color: #f2f2f2;">
        <th>Nome</th>
        <th>Função</th>
        <th>GitHub</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Aline Oliveira</td>
        <td>Desenvolvedora Back-end</td>
        <td><a href="https://github.com/alineop120" target="_blank">@alineop120</a></td>
      </tr>
      <tr>
        <td>Camila Mendes</td>
        <td>Desenvolvedora Front-end</td>
        <td><a href="#" target="_blank"></a></td>
      </tr>
      <tr>
        <td>Ana Beatriz Amorim</td>
        <td>Analista de Requisitos</td>
        <td><a href="https://github.com/Anabamorim" target="_blank">@Anabamorim</a></td>
      </tr>
    </tbody>
  </table>
</div>

<h2>📋 Observações</h2>
<ul>
  <li>NPCs atualizam suas posições a cada segundo no backend, enviadas para o frontend.</li>
  <li>O mapa é dividido em células de 40x40px para facilitar movimentação e colisões.</li>
  <li>Use o componente <code>NPCs.js</code> para renderizar NPCs na tela.</li>
</ul>

<h2>🤝 Contato</h2>
<p>Abra issues para dúvidas, sugestões ou contribuições.</p>
