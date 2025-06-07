import React, { useEffect, useState } from 'react';
import axios from 'axios';

import PlayerMovement from './components/Player/PlayerMovement';
import GameMap from './components/GameMap/GameMap';
import { isCellWalkable, getCellType } from './components/GameMap/mapUtils';
import NPCs from './components/NPCs/NPCs';

function App() {
    const [jogador, setJogador] = useState(null);
    const [carregando, setCarregando] = useState(true);
    const [playerPos, setPlayerPos] = useState({ x: 0, y: 0 });
    const [npcs, setNpcs] = useState({});
    const [localAtual, setLocalAtual] = useState(null);

    useEffect(() => {
        const fetchEstado = () => {
            axios.get('http://localhost:5000/estado')
                .then(response => {
                    setJogador(response.data.jogador);
                    setNpcs({
                        npc1: response.data.npc1,
                        npc2: response.data.npc2
                    });
                    //setPlayerPos(response.data.jogador.posicao);
                })
                .catch(error => {
                    console.error("Erro ao buscar estado:", error);
                });
        };

        fetchEstado(); // primeira chamada
        const intervalo = setInterval(fetchEstado, 1000); // uma por segundo

        return () => clearInterval(intervalo); // limpar ao desmontar
    }, []); // ← array de dependências vazio!

    const handlePositionChange = (newPos) => {
        const cellX = Math.floor(newPos.x / 40);
        const cellY = Math.floor(newPos.y / 40);

        if (!isCellWalkable(cellX, cellY)) return;

        // Verifica se algum NPC já está nessa posição
        const temColisaoComNPC = Object.values(npcs).some(npc =>
            npc.posicao.x === newPos.x && npc.posicao.y === newPos.y
        );
        if (temColisaoComNPC) return;

        setPlayerPos(newPos);

        const cellType = getCellType(cellX, cellY);
        if (cellType === 'G') setLocalAtual('guilda');
        else if (cellType === 'L') setLocalAtual('loja');
        else setLocalAtual(null);

        axios.post('http://localhost:5000/mover', newPos)
            .then(res => console.log(res.data.mensagem))
            .catch(err => console.error('Erro ao mover:', err));
    };

    if (carregando) return <p>Carregando...</p>;

    return (
        <div style={{ maxWidth: 600, margin: '20px auto', fontFamily: 'Arial' }}>
            <h1>Status do Jogador</h1>
            {jogador ? (
                <div style={{ marginBottom: 20 }}>
                    <p><strong>Nome:</strong> {jogador.nome}</p>
                    <p><strong>Vida:</strong> {jogador.vida}</p>
                    <p><strong>Recursos:</strong> {jogador.recursos}</p>
                    <p><strong>Moedas:</strong> {jogador.moedas}</p>
                </div>
            ) : (
                <p>Erro ao carregar dados.</p>
            )}

            <h2>Área de Jogo</h2>
            <div style={{
                position: 'relative',
                width: 420,
                height: 438,
                border: '2px solid #333',
                backgroundColor: '#f0f0f0',
                overflow: 'hidden',
                borderRadius: 10,
                marginBottom: 10
            }}>
                <GameMap playerPos={playerPos} />
                <PlayerMovement playerPos={playerPos} onPositionChange={handlePositionChange} />
                <NPCs npcs={npcs} />
            </div>

            <h2>Posição Atual</h2>
            <p>X: {playerPos.x} | Y: {playerPos.y}</p>
        </div>
    );
}

export default App;