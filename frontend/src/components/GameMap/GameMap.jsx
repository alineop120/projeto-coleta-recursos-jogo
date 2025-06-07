import React from 'react';
import { mapa } from './mapData';

export default function GameMap({ playerPos }) {
    return (
        <div style={{
            display: 'grid',
            gridTemplateColumns: `repeat(${mapa[0].length}, 40px)`,
            gap: '2px'
        }}>
            {mapa.flatMap((linha, y) =>
                linha.map((celula, x) => {
                    const isPlayerHere = playerPos.x === x * 40 && playerPos.y === y * 40;
                    let bg = 'white';
                    let label = '';

                    switch (celula) {
                        case 'X':
                            bg = 'gray';
                            break;
                        case 'N':
                            bg = 'green';
                            label = '🌳';
                            break;
                        case 'G':
                            bg = '#FFD700';
                            label = '🏰';
                            break;
                        case 'L':
                            bg = '#ADD8E6';
                            label = '🏪';
                            break;
                        default:
                            bg = 'white';
                    }

                    return (
                        <div
                            key={`${x}-${y}`}
                            style={{
                                width: 40,
                                height: 40,
                                backgroundColor: bg,
                                border: '1px solid #ccc',
                                display: 'flex',
                                justifyContent: 'center',
                                alignItems: 'center',
                                fontSize: '24px',
                                userSelect: 'none',
                            }}
                        >
                            {label}
                        </div>
                    );
                })
            )}
        </div>
    );
}
