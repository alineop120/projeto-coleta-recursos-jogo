// src/App.jsx
import React, { useContext } from 'react';
import { GameContext } from './context/GameContext';
import GameMap from './components/GameMap/GameMap';
import PlayerMovement from './components/Player/PlayerMovement';
import NPCList from './components/NPCs/NPCList';
import Loja from './components/LojaGuilda/Loja';
import Guilda from './components/LojaGuilda/Guilda';

function App() {
    console.log('App renderizado');
    const { player, npcs, recursos } = useContext(GameContext);

    if (!player) return <div>Carregando...</div>;

    return (
        <div>
            <GameMap playerPos={player.pos} npcs={npcs} recursos={recursos} />
            <PlayerMovement playerPos={player.pos} />
            <NPCList npcs={npcs} />
            <Loja />
            <Guilda />
        </div>
    );
}

export default App;
