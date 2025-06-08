import React, { useEffect, useState } from 'react';
import axios from 'axios';

import './styles/App.css';

import Player from './components/Player/Player';
import GameMap from './components/Maps/GameMap';
import { isCellWalkable, getCellType } from './components/Maps/mapUtils';
import NPCs from './components/NPCs/NPCs';
import Resources from './components/Resources/Resources';

import Loja from './components/Maps/Locations/Loja';
import Guilda from './components/Maps/Locations/Guilda';

function App() {
    const [jogador, setJogador] = useState(null);
    const [carregando, setCarregando] = useState(true);
    const [playerPos, setPlayerPos] = useState({ x: 0, y: 0 });
    const [npcs, setNpcs] = useState({});
    const [recursos, setRecursos] = useState([]);
    const [localAtual, setLocalAtual] = useState(null);

    const fetchEstado = () => {
        axios.get('http://localhost:5000/estado')
            .then(response => {
                setJogador(response.data.jogador);
                setNpcs({
                    npc1: response.data.npc1,
                    npc2: response.data.npc2
                });
                setRecursos(response.data.recursos || []);
                setCarregando(false);
            })
            .catch(error => {
                console.error("Erro ao buscar estado:", error);
            });
    };

    const coletarRecurso = (recurso) => {
        axios.post('http://localhost:5000/coletar', {
            x: recurso.x,
            y: recurso.y
        }, {
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(() => {
                fetchEstado(); // Atualiza dados após coleta
            })
            .catch(err => {
                console.error("Erro ao coletar recurso:", err);
            });
    };

    useEffect(() => {
        fetchEstado();
        const intervalo = setInterval(fetchEstado, 1000);
        return () => clearInterval(intervalo);
    }, []);

    // Função só para atualizar localAtual quando a posição muda
    const handlePositionChange = (newPos) => {
        const cellX = Math.floor(newPos.x / 40);
        const cellY = Math.floor(newPos.y / 40);

        if (!isCellWalkable(cellX, cellY)) return;

        // Verifica colisão com NPCs
        const temColisaoComNPC = Object.values(npcs).some(npc =>
            npc.posicao.x === newPos.x && npc.posicao.y === newPos.y
        );
        if (temColisaoComNPC) return;

        setPlayerPos(newPos);

        const cellType = getCellType(cellX, cellY);
        if (cellType === 'G') setLocalAtual('guilda');
        else if (cellType === 'L') setLocalAtual('loja');
        else setLocalAtual(null);
    };

    if (carregando) return <p>Carregando...</p>;

    return (
        <div className="app-container">
            <div className="header">
                <div className="status-jogador">
                    <h1>Status do Jogador</h1>
                    {jogador ? (
                        <div>
                            <p><strong>Nome:</strong> {jogador.nome}</p>
                            <p><strong>Vida:</strong> {jogador.vida}</p>
                            <p><strong>Recursos:</strong> {jogador.recursos}</p>
                            <p><strong>Moedas:</strong> {jogador.moedas}</p>
                        </div>
                    ) : (
                        <p>Erro ao carregar dados.</p>
                    )}
                </div>

                <div className="interacoes">
                    {localAtual === 'loja' && <Loja onCompraRealizada={fetchEstado} />}
                    {localAtual === 'guilda' && <Guilda />}
                </div>
            </div>

            <div className="main-content">
                <div className="area-jogo-header">
                    <h2>Área de Jogo</h2>
                    <div className="posicao-atual">
                        <strong>Posição Atual:</strong> X: {playerPos.x} | Y: {playerPos.y}
                    </div>
                </div>

                <div className="area-jogo">
                    <GameMap playerPos={playerPos} />
                    <Player
                        playerPos={playerPos}
                        setPlayerPos={setPlayerPos}
                        recursos={recursos}
                        fetchEstado={fetchEstado}
                    />
                    <NPCs npcs={npcs} />
                    <Resources recursos={recursos} onColetar={coletarRecurso} />
                </div>
            </div>
        </div>
    );
}

export default App;
