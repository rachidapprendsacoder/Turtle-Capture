import time

screen_size_x = 1900  # pour un fonctionnement du jeu optimal, cette valeur doit être un multiple de 38
screen_size_y = (13 / 19) * screen_size_x
sq_size = 2 / 19 * screen_size_x
path_size = 0.5 * sq_size
font_size = int(screen_size_x/45)

map_size = (4, 6)

game_duration = 69

start_time = time.time()
