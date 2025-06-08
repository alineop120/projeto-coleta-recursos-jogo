import React from 'react';

function Resources({ recursos, onColetar }) {
    return (
        <>
            {recursos.map((recurso, index) => (
                <div
                    key={index}
                    style={{
                        position: 'absolute',
                        left: recurso.x,
                        top: recurso.y,
                        width: 40,
                        height: 40,
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        fontSize: 24,
                        cursor: 'pointer',
                    }}
                    onClick={() => onColetar(recurso)}
                >
                    💎
                </div>
            ))}
        </>
    );
}

export default Resources;