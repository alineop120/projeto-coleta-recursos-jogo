import axios from 'axios';

export const comprarItem = (item) => {
    return axios.post('http://localhost:5000/comprar', { item });
};
