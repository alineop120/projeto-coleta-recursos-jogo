import React, { useContext } from 'react';
import { GameContext } from '../../context/GameContext';
import { moverPlayer } from '../../services/api';

export default function PlayerMovement() {
    const { player, setPlayer } = useContext(GameContext);

    if (!player) return null;

    const move = async (dx, dy) => {
        const newPos = { x: player.pos.x + dx, y: player.pos.y + dy };

        try {
            await moverPlayer(newPos);
            // Atualiza localmente, o socket também pode atualizar, mas para resposta imediata:
            setPlayer(prev => ({ ...prev, pos: newPos }));
        } catch (error) {
            console.error('Erro ao mover player:', error);
        }
    };

    return (
        <div style={{ marginTop: 20 }}>
            <button onClick={() => move(0, -1)}>↑</button>
            <div>
                <button onClick={() => move(-1, 0)}>←</button>
                <button onClick={() => move(1, 0)}>→</button>
            </div>
            <button onClick={() => move(0, 1)}>↓</button>
        </div>
    );
}