import React from 'react';

export default function NPCs({ npcs }) {
    return (
        <>
            {Object.entries(npcs).map(([nome, npc]) => (
                <div
                    key={nome}
                    style={{
                        position: 'absolute',
                        width: '40px',
                        height: '40px',
                        backgroundColor: 'pink',
                        borderRadius: '50%',
                        left: npc.posicao.x,
                        top: npc.posicao.y,
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        color: 'white',
                        fontWeight: 'bold',
                        transition: 'left 0.2s, top 0.2s',
                    }}
                >
                    {nome.toUpperCase()}
                </div>
            ))}
        </>
    );
}