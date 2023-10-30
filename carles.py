import random
from constants import *
from turtles import carles, speed
from utils import lign_pos, column_pos
from move import move

def carles_apparition():
    if random.choice(['apparition', 'no apparition']) == 'apparition':
        carles.showturtle()
        direction = random.choice(['horizontal','vertical'])
        carles_advance(direction)
        carles.hideturtle()

def carles_advance(direction):
    if direction == 'horizontal':
        lign_position = random.randint(0, map_size[0])
        carles.goto(-screen_size_x/2  , lign_pos(lign_position) + path_size / 2)
        for advance in range(int(screen_size_x// speed[carles])):
            move(carles, 'right', 'bot')
    else:
        column_position = random.randint(0, map_size[1])
        carles.goto(column_pos(column_position) - path_size/2, -screen_size_y/2)
        for advance in range(int(screen_size_y // speed[carles])):
            move(carles, 'down', 'bot')
