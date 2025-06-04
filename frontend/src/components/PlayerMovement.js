import React, { useState, useEffect } from 'react';

export default function PlayerMovement({ onPositionChange }) {
    const [pos, setPos] = useState({ x: 0, y: 0 });

    useEffect(() => {
        const handleKeyDown = (e) => {
            setPos(prev => {
                const step = 10;
                const size = 40;
                const maxX = 400 - size;
                const maxY = 400 - size;

                let newPos;
                switch (e.key.toLowerCase()) {
                    case 'w':
                        newPos = { x: prev.x, y: Math.max(prev.y - step, 0) };
                        break;
                    case 's':
                        newPos = { x: prev.x, y: Math.min(prev.y + step, maxY) };
                        break;
                    case 'a':
                        newPos = { x: Math.max(prev.x - step, 0), y: prev.y };
                        break;
                    case 'd':
                        newPos = { x: Math.min(prev.x + step, maxX), y: prev.y };
                        break;
                    default:
                        return prev;
                }

                if (onPositionChange) {
                    onPositionChange(newPos);
                }
                return newPos;
            });
        };

        window.addEventListener('keydown', handleKeyDown);
        return () => window.removeEventListener('keydown', handleKeyDown);
    }, [onPositionChange]);

    return (
        <div style={{
            position: 'absolute',
            width: '40px',
            height: '40px',
            backgroundColor: 'blue',
            borderRadius: 5,
            left: pos.x,
            top: pos.y,
            transition: 'left 0.1s, top 0.1s'
        }} />
    );
}
