import React from 'react';
import { comprarItem } from '../../services/api';

export default function Loja() {
    const comprar = async (item) => {
        try {
            await comprarItem(item);
            alert(`${item} comprado com sucesso!`);
        } catch (e) {
            alert('Erro na compra');
        }
    };

    return (
        <div>
            <h4>Loja</h4>
            <button onClick={() => comprar('espada')}>Comprar Espada</button>
            <button onClick={() => comprar('poção')}>Comprar Poção</button>
        </div>
    );
}