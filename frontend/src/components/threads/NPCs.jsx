import React from 'react';

export default function NPCs({ npcs }) {
    if (!npcs) return null;

    return (
        <>
            {Object.entries(npcs).map(([nome, data]) => (
                <div key={nome}
                    style={{
                        position: 'absolute',
                        width: '40px',
                        height: '40px',
                        backgroundColor: 'hotpink',
                        borderRadius: '4px',
                        left: data.posicao.x,
                        top: data.posicao.y,
                        transition: 'left 0.5s, top 0.5s'
                    }}
                    title={nome}
                />
            ))}
        </>
    );
}