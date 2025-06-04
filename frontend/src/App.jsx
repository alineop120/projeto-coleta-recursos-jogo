import React, { useEffect, useState } from 'react';
import axios from 'axios';

import PlayerMovement from './components/PlayerMovement';
import GameMap from './components/map/GameMap';
import { isCellWalkable, getCellType } from './components/map/mapUtils';
import NPCs from './components/threads/NPCs'; // importar o novo componente

function App() {
    const [jogador, setJogador] = useState(null);
    const [carregando, setCarregando] = useState(true);
    const [playerPos, setPlayerPos] = useState({ x: 0, y: 0 });

    useEffect(() => {
        axios.get('http://localhost:5000/estado')
            .then(response => {
                setJogador(response.data.jogador);
                setPlayerPos(response.data.jogador.posicao);
                setCarregando(false);
            })
            .catch(error => {
                console.error("Erro ao buscar estado:", error);
                setCarregando(false);
            });
    }, []);

    const[localAtual, setLocalAtual] = useState(null);

    const handlePositionChange = (newPos) => {
        const cellX = Math.floor(newPos.x / 40);
        const cellY = Math.floor(newPos.y / 40);

        if (!isCellWalkable(cellX, cellY)) return;

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
                <PlayerMovement onPositionChange={handlePositionChange} />
                <NPCs npcs={NPCs} />
            </div>

            <h2>Posição Atual</h2>
            <p>X: {playerPos.x} | Y: {playerPos.y}</p>
        </div>
    );
}

export default App;