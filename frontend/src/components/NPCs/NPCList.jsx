import React from 'react';

export default function NPCList({ npcs }) {
    return (
        <div>
            <h4>NPCs</h4>
            <ul>
                {Object.entries(npcs).map(([name, pos]) => (
                    <li key={name}>{name} - ({pos.x}, {pos.y})</li>
                ))}
            </ul>
        </div>
    );
}