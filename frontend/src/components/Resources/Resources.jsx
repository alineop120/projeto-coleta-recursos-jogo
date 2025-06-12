import React, { useContext } from 'react';
import { GameContext } from '../../context/GameContext';

const STEP = 40;

export default function Resources() {
    const { resources } = useContext(GameContext);

    return (
        <>
            {resources.map((recurso, index) => (
                <div
                    key={index}
                    style={{
                        position: 'absolute',
                        left: recurso.x,
                        top: recurso.y,
                        width: STEP,
                        height: STEP,
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        fontSize: 24,
                        cursor: 'pointer',
                    }}
                    title={`Recurso em (${recurso.x}, ${recurso.y})`}
                >
                    💎
                </div>
            ))}
        </>
    );
}