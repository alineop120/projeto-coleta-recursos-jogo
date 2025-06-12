// src/context/GameContext.jsx
import React, { createContext, useState, useEffect } from 'react';
import { getPlayer, getNPCs, getRecursos } from '../services/api';
import socket from '../services/socket';

export const GameContext = createContext();

export function GameProvider({ children }) {
    const [player, setPlayer] = useState(null);
    const [npcs, setNpcs] = useState([]);
    const [recursos, setRecursos] = useState([]);

    useEffect(() => {
        async function fetchInitialData() {
            try {
                const playerData = await getPlayer();
                const npcsData = await getNPCs();
                const recursosData = await getRecursos();
                setPlayer(playerData);
                setNpcs(npcsData);
                setRecursos(recursosData);
            } catch (error) {
                console.error('Erro ao carregar dados iniciais:', error);
            }
        }
        fetchInitialData();

        socket.on('npc_update', setNpcs);
        socket.on('player_update', setPlayer);
        socket.on('recursos_update', setRecursos);

        return () => {
            socket.off('npc_update');
            socket.off('player_update');
            socket.off('recursos_update');
        };
    }, []);

    return (
        <GameContext.Provider value={{ player, setPlayer, npcs, setNpcs, recursos, setRecursos }}>
            {children}
        </GameContext.Provider>
    );
}