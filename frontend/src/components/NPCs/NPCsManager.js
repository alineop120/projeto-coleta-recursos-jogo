import { mapa } from '../Maps/mapData';

const NPCManager = (() => {
    const npcs = {
        joao: { gridX: 5, gridY: 5 },
        maria: { gridX: 8, gridY: 3 },
    };

    function moverNPC(npc) {
        const direcoes = [
            { dx: 0, dy: -1 }, // cima
            { dx: 1, dy: 0 },  // direita
            { dx: 0, dy: 1 },  // baixo
            { dx: -1, dy: 0 }, // esquerda
        ];

        const direcao = direcoes[Math.floor(Math.random() * direcoes.length)];
        const novoX = npc.gridX + direcao.dx;
        const novoY = npc.gridY + direcao.dy;

        // Verifica se a célula é válida e não é parede ('X')
        if (
            mapa[novoY] &&
            mapa[novoY][novoX] &&
            mapa[novoY][novoX] !== 'X'
        ) {
            npc.gridX = novoX;
            npc.gridY = novoY;
        }
    }

    function atualizarNPCs() {
        for (const nome in npcs) {
            moverNPC(npcs[nome]);
        }
    }

    function getNPCs() {
        // Converte gridX/Y para coordenadas absolutas de tela
        const npcRenderizados = {};
        for (const nome in npcs) {
            const { gridX, gridY } = npcs[nome];
            npcRenderizados[nome] = {
                gridX,
                gridY,
                posicao: {
                    x: gridX * 40,
                    y: gridY * 40,
                },
            };
        }
        return npcRenderizados;
    }

    return {
        atualizarNPCs,
        getNPCs,
    };
})();

export default NPCManager;
