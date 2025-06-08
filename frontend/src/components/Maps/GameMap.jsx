import React from 'react';
import { mapa } from './mapData';
import { getCellType } from './mapUtils';

const CELL_SIZE = 40;

export default function GameMap({ playerPos }) {
    return (
        <div
            style={{
                display: 'grid',
                gridTemplateColumns: `repeat(${mapa[0].length}, ${CELL_SIZE}px)`,
                gap: '2px',
                userSelect: 'none',
            }}
            role="grid"
        >
            {mapa.flatMap((linha, y) =>
                linha.map((celula, x) => {
                    const isPlayerHere = playerPos.x === x * CELL_SIZE && playerPos.y === y * CELL_SIZE;

                    let bg = 'white';
                    let label = '';

                    switch (getCellType(x, y)) {
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
                            role="gridcell"
                            aria-label={`Célula ${x}, ${y}`}
                            style={{
                                width: CELL_SIZE,
                                height: CELL_SIZE,
                                backgroundColor: bg,
                                boxShadow: isPlayerHere ? '0 0 8px 3px rgba(0, 123, 255, 0.7)' : 'none',
                                border: '1px solid #ccc',
                                display: 'flex',
                                justifyContent: 'center',
                                alignItems: 'center',
                                fontSize: '24px',
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
