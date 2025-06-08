import React from 'react';
import axios from 'axios';
import PlayerMovement from './PlayerMovement';

export default function Player({ playerPos, setPlayerPos, recursos, fetchEstado }) {

    const handlePositionChange = (newPos) => {
        axios.post('http://localhost:5000/mover', { x: newPos.x, y: newPos.y })
            .then(() => {
                setPlayerPos(newPos);

                const recursoNaPos = recursos.some(r => r.x === newPos.x && r.y === newPos.y);
                if (recursoNaPos) {
                    return axios.post('http://localhost:5000/coletar', { x: newPos.x, y: newPos.y })
                        .then(() => fetchEstado());
                } else {
                    return fetchEstado();
                }
            })
            .catch(err => console.error('Erro na movimentação ou coleta:', err));
    };

    return (
        <PlayerMovement
            playerPos={playerPos}
            onPositionChange={handlePositionChange}
        />
    );
}