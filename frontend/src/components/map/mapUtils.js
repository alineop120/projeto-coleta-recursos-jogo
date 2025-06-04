// src/components/map/mapUtils.js
import { mapa } from './mapData';

export function isCellWalkable(x, y) {
    if (y < 0 || y >= mapa.length || x < 0 || x >= mapa[0].length) return false;
    return mapa[y][x] !== 'X';  // 'X' é obstáculo
}

export function getCellType(x, y) {
    if (y < 0 || y >= mapa.length || x < 0 || x >= mapa[0].length) return null;
    return mapa[y][x];
}