import React, { useState } from 'react';
import { comprarItem } from '../../../services/api';

function Loja({ onCompraRealizada }) {
    const [loading, setLoading] = useState(false);
    const [mensagem, setMensagem] = useState('');

    const handleComprar = async (item) => {
        setLoading(true);
        setMensagem('');
        try {
            const response = await comprarItem(item);
            setMensagem(`Compra de ${item} realizada com sucesso!`);
            if (onCompraRealizada) {
                onCompraRealizada(); // para atualizar o estado geral no App.jsx
            }
        } catch (error) {
            setMensagem(`Erro ao comprar ${item}: ${error.response?.data?.mensagem || error.message}`);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div style={{ padding: 10, border: '1px solid #999', borderRadius: 5, backgroundColor: '#fff' }}>
            <h3>Loja</h3>
            <button disabled={loading} onClick={() => handleComprar('espada')}>Comprar Espada</button>
            <button disabled={loading} onClick={() => handleComprar('mochila')}>Comprar Mochila</button>
            <button disabled={loading} onClick={() => handleComprar('poção')}>Comprar Poção</button>
            {mensagem && <p>{mensagem}</p>}
        </div>
    );
}

export default Loja;