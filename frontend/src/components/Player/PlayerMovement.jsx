import React, { useEffect } from 'react';

export default function PlayerMovement({ playerPos, onPositionChange }) {
    useEffect(() => {
        const step = 1;
        const handleKeyDown = (e) => {
            let dx = 0, dy = 0;
            switch (e.key.toLowerCase()) {
                case 'w': dy = -step; break;
                case 's': dy = step; break;
                case 'a': dx = -step; break;
                case 'd': dx = step; break;
                default: return;
            }
            onPositionChange({ x: playerPos.x + dx, y: playerPos.y + dy });
        };

        window.addEventListener('keydown', handleKeyDown);
        return () => window.removeEventListener('keydown', handleKeyDown);
    }, [playerPos, onPositionChange]);

    return null;
}