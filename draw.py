from constants import screen_size_y, map_size, sq_size
from turtles import *
from map_state import sq_list
from constants import game_duration

window = ttl.Screen()
window.setup(width=screen_size_x, height=screen_size_y)
window.tracer(n=1, delay=0)

window.title(f'Turtle Capture ({game_duration}s)')
sq_color = {player1: 'red', player2: 'blue', bot_player: 'green', carles: 'black'}


# Dessine chaque carré
def draw_map():
    for i in range(map_size[0]):
        for j in range(map_size[1]):
            draw_square(builder, sq_list[i][j][0])


def draw_captured_square(i, j, turtle0):
    if sq_list[i][j][2] == 4 * [player_color[turtle0]] and sq_list[i][j][0] != player_color[turtle0]:
        # si les quatre cotés du carré sont coloriés de la couleur de la turtle et que le carré n'est pas déjâ colorié
        draw_square(builder, sq_list[i][j][0], sq_color[turtle0])  # colorie le carré de la couleur correspondante
        sq_list[i][j][1] = turtle_color[turtle0]  # écrit dans la liste que le carré est colorié
    elif sq_list[i][j][1] != 'black':
        draw_square(builder, sq_list[i][j][0])  # sinon, colorie le carré en noir
        sq_list[i][j][1] = 'black'  # écrit dans la liste que le carré est noir


# Dessine un carré
def draw_square(turtle0, pos, color='black', size=sq_size):
    if size == sq_size:
        size = size - screen_size_x / 95
        pos = pos[0] + screen_size_x / 190, pos[1] - screen_size_x / 190
    turtle0.color(color)
    turtle0.goto(pos)
    turtle0.begin_fill()
    turtle0.setheading(0)
    turtle0.forward(size)
    turtle0.right(90)
    turtle0.forward(size)
    turtle0.right(90)
    turtle0.forward(size)
    turtle0.right(90)
    turtle0.forward(size)
    turtle0.end_fill()


# dessine un rectangle entre les carrés
def draw_area(turtle0, pos, orientation, color=''):
    turtle0.color(color)
    if orientation == 'h':
        turtle0.setheading(0)
        turtle0.goto(pos[0] + path_size, pos[1])
    else:
        turtle0.setheading(90)
        turtle0.goto(pos[0], pos[1] + sq_size / 2)
    turtle0.begin_fill()
    turtle0.right(90)
    turtle0.forward(path_size / 2)
    turtle0.right(90)
    turtle0.forward(sq_size)
    turtle0.right(90)
    turtle0.forward(path_size)
    turtle0.right(90)
    turtle0.forward(sq_size)
    turtle0.right(90)
    turtle0.forward(path_size / 2)
    turtle0.end_fill()


def draw_circle_power(pos, color):
    builder.goto(pos)
    builder.fillcolor(color)
    builder.begin_fill()
    builder.circle(path_size / 2)
    builder.end_fill()
