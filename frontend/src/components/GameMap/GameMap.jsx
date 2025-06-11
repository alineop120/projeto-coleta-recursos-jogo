import React from 'react';
import { mapa } from './mapUtils';

const CELL_SIZE = 40;

export default function GameMap({ playerPos, npcs }) {
    return (
        <div style={{
            display: 'grid',
            gridTemplateColumns: `repeat(${mapa[0].length}, ${CELL_SIZE}px)`
        }}>
            {mapa.flatMap((row, y) =>
                row.map((cel, x) => {
                    const isPlayer = playerPos.x === x && playerPos.y === y;
                    const npcHere = Object.values(npcs).find(n => n.x === x && n.y === y);
                    const color = cel === 'X' ? 'gray' : cel === 'L' ? '#ADD8E6' : cel === 'G' ? '#FFD700' : 'white';

                    return (
                        <div key={`${x}-${y}`} style={{
                            width: CELL_SIZE,
                            height: CELL_SIZE,
                            backgroundColor: color,
                            border: '1px solid black',
                            position: 'relative'
                        }}>
                            {isPlayer && <div style={{
                                position: 'absolute',
                                width: '100%',
                                height: '100%',
                                backgroundColor: 'blue',
                                opacity: 0.6
                            }} />}
                            {npcHere && <div style={{
                                position: 'absolute',
                                width: '100%',
                                height: '100%',
                                backgroundColor: 'pink',
                                opacity: 0.5
                            }} />}
                        </div>
                    );
                })
            )}
        </div>
    );
}