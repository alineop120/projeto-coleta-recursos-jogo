const express = require('express');
const cors = require('cors');

const app = express();
const PORT = 5000;

app.use(cors());               // Libera CORS para todas as origens
app.use(express.json());       // Para interpretar JSON no corpo das requisições

// Estado inicial do jogador (exemplo)
let jogador = {
    nome: 'Herói',
    vida: 100,
    recursos: 50,
    moedas: 200,
    posicao: { x: 0, y: 0 }
};

// Rota para retornar o estado do jogador
app.get('/estado', (req, res) => {
    res.json({ jogador });
});

// Rota para atualizar a posição do jogador
app.post('/mover', (req, res) => {
    const { x, y } = req.body;

    if (typeof x !== 'number' || typeof y !== 'number') {
        return res.status(400).json({ mensagem: 'Posição inválida' });
    }

    jogador.posicao = { x, y };

    console.log(`Jogador moveu para: (${x}, ${y})`);

    res.json({ mensagem: 'Posição atualizada com sucesso' });
});

app.listen(PORT, () => {
    console.log(`Servidor rodando na porta ${PORT}`);
});
