from turtles import speed
from constants import *
from squares import update_squares

# les modulos permettent à la turtle de se téléporter d'un bout à l'autre de l'écran
def add_tuples(pos, v):
    return ((pos[0] + v[0] + screen_size_x / 2) % screen_size_x) - screen_size_x / 2, \
           ((pos[1] + v[1] + screen_size_y / 2) % screen_size_y) - screen_size_y / 2
def move(turtle0, dir, player='human'):
    setheading = {'up': 90, 'down': 270, 'left': 180, 'right': 0}
    movement = {'up': (0, speed[turtle0]), 'down': (0, -speed[turtle0]), 'right': (speed[turtle0], 0), 'left': (-speed[turtle0], 0)}
    if allowed_pos(add_tuples(turtle0.pos(), movement[dir])):  # vérifie que la position suivante est autorisée
        turtle0.setheading(setheading[dir])  # oriente la tête
        update_squares(turtle0, add_tuples(turtle0.pos(), movement[dir]))
        turtle0.goto(add_tuples(turtle0.pos(), movement[dir]))  # déplace la tortue


# Définir les postions autorisées
def allowed_pos(pos):
    if 0 <= (pos[0] + path_size / 2) % (sq_size + path_size) <= path_size:  # si la position est autorisé en x
        return True
    if 0 <= (pos[1] + path_size / 2) % (sq_size + path_size) <= path_size:  # si la position est autorisé en y
        return True
    # on peut sortir de l'écran
    if screen_size_y / 2 < pos[1] or pos[1] <= -screen_size_y / 2 or screen_size_x / 2 <= pos[0] or pos[0] <= -screen_size_x / 2:
        return True
    return False
