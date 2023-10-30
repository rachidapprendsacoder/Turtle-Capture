from constants import screen_size_x, screen_size_y, path_size, sq_size

# les modulos permettent à la turtle de se téléporter d'un bout à l'autre de l'écran
def add_tuples(pos, v):
    return ((pos[0] + v[0] + screen_size_x / 2) % screen_size_x) - screen_size_x / 2, \
           ((pos[1] + v[1] + screen_size_y / 2) % screen_size_y) - screen_size_y / 2

def lign_pos(i):
    return screen_size_y / 2 - path_size - (sq_size + path_size) * i


def column_pos(j):
    return -screen_size_x / 2 + path_size + (sq_size + path_size) * j
