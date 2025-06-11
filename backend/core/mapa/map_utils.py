from core.mapa.map_data import mapa

def is_cell_walkable(x, y):
    return 0 <= y < len(mapa) and 0 <= x < len(mapa[0]) and mapa[y][x] != 'X'

def get_cell_type(x, y):
    if 0 <= y < len(mapa) and 0 <= x < len(mapa[0]):
        return mapa[y][x]
    return None