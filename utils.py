from constants import screen_size_x, screen_size_y, path_size, sq_size

def lign_pos(i):
    return screen_size_y / 2 - path_size - (sq_size + path_size) * i


def column_pos(j):
    return -screen_size_x / 2 + path_size + (sq_size + path_size) * j
