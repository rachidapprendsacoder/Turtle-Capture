import random
from constants import *
from turtles import deleter, speed
from utils import lign_pos, column_pos
from move import move

def deleter_apparition():
    if random.choice(['apparition', 'no apparition', 'no apparition', 'no apparition']) == 'apparition':  # choisis si carles apparait ou non
        deleter.showturtle()
        direction = random.choice(['horizontal', 'vertical'])
        deleter_advance(direction)
        deleter.hideturtle()

def deleter_advance(direction):
    if direction == 'horizontal':
        lign_position = random.randint(0, map_size[0])
        deleter.goto(-screen_size_x/2, lign_pos(lign_position) + path_size / 2)
        for advance in range(int(screen_size_x // speed[deleter])):
            move(deleter, 'right', 'bot')
    else:
        column_position = random.randint(0, map_size[1])
        deleter.goto(column_pos(column_position) - path_size/2, -screen_size_y/2)
        for advance in range(int(screen_size_y // speed[deleter])):
            move(deleter, 'down', 'bot')
