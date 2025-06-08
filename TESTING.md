# Como Rodar os Testes do Projeto

## Estrutura do Projeto (referência)
```bash
projeto-coleta-recursos-jogo/
├── backend/
│   ├── routes/
│   │   ├── player.py
│   │   ├── npc.py
│   ├── tests/
│   │   └── test_player_routes.py
│   ├── app.py
│   └── requirements.txt
├── frontend/
│   └── ...
├── README.md
```

## 1. Preparação do Ambiente Backend

1. Preparação do Ambiente Backend
Abra o terminal e navegue até a pasta backend:
```bash
cd backend
```

2. Crie e ative o ambiente virtual:
- Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

- Linux/macOS:
```bash
python -m venv .venv
source .venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
pip install pytest pytest-flask
```

## 2. Ajuste no Arquivo de Testes

Para garantir que o Python reconheça os módulos do backend, adicione no início de cada arquivo de teste (ex: test_player_routes.py) o seguinte código:
```python
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
```

## 3. Rodando os Testes

Você pode rodar os testes de diferentes formas, dependendo de onde estiver no terminal:

- Na raiz do projeto (pasta acima de backend):
```bash
pytest backend/tests/
```

- Dentro da pasta backend:
```bash
pytest tests/
```

- Dentro da pasta backend/tests:
```bash
pytest
```

## 4. Comandos Úteis
- Rodar testes com saída detalhada:
```bash
pytest backend/tests/ -v
```

- Rodar um teste específico:
```bash
pytest backend/tests/test_player_routes.py::test_nome_da_funcao
```

## 5. Erros Comuns e Soluções
- Erro ModuleNotFoundError: No module named 'routes'
    - Verifique se o ajuste do sys.path foi adicionado no arquivo de teste.
    - Garanta que você esteja rodando o pytest a partir da raiz do projeto ou que o caminho está correto.

- Nenhum teste encontrado
    - Confira se o arquivo e as funções de teste seguem o padrão test_*.py e test_*().
    - Certifique-se de estar no diretório correto para rodar o pytest.

## 6. Observações
- Os testes são importantes para garantir que as funcionalidades do backend estejam funcionando corretamente.
- Sempre que adicionar uma nova funcionalidade, não esqueça de criar os testes correspondentes.
- Para frontend, utilize ferramentas próprias como jest ou react-testing-library.

> Qualquer dúvida, estamos à disposição para ajudar!