import axios from 'axios';

const API = axios.create({ baseURL: 'http://localhost:5000' });

export const getPlayer = async () => {
    const { data } = await API.get('/player/status');
    return data;
};

export const moverPlayer = async (pos) => {
    await API.post('/player/mover', pos);
};

export const getNPCs = async () => {
    const { data } = await API.get('/npc/estado');
    return data;
};

export const getRecursos = async () => {
    const { data } = await API.get('/recursos/estado');
    return data;
};

export const comprarItem = async (item) => {
    return API.post('/player/comprar', { item });
};