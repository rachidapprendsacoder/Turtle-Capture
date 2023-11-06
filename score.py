import time
from draw import window
from turtles import *
from constants import screen_size_y, map_size, font_size
from map_state import sq_list
from music import *


def score():
    window.clearscreen()
    music_score()
    score_player = {player1: 0, player2: 0, bot_player: 0}

    for i in range(map_size[0]):
        for j in range(map_size[1]):
            if sq_list[i][j][2] == 4 * [player_color[player1]]:  # si les quatre cotés du carré sont coloriés de la couleur de la turtle1
                score_player[player1] += 1
            elif sq_list[i][j][2] == 4 * [player_color[player2]]:  # si les quatre cotés du carré sont coloriés de la couleur de la turtle2
                score_player[player2] += 1

    set_turtle(player1, (-path_size * 2, 0), color='red')
    set_turtle(player2, (path_size * 2, 0), color='blue')
    player1.write(f"J'ai un score de {score_player[player1]} pts", font=('ArcadeClassic', font_size, 'bold'), align='right')
    player2.write(f"J'ai un score de {score_player[player2]} pts", font=('ArcadeClassic', font_size, 'bold'), align='left')
#    bot_player.write(f"J'ai un score de {score_player[bot_player]} pts", font=('ArcadeClassic', timer_size, 'bold'))
    print(f"la turtle verte a un score de {score_player[bot_player]} pts")


    if score_player[player1] > score_player[player2]:
        print('La turtle rouge a gagné !')
        print_winner(player1)
    elif score_player[player1] == score_player[player2]:
        set_turtle(painter, (0, screen_size_y / 4), color='#404040')
        painter.write(f"Egalite", font=('ArcadeClassic', font_size * 2, 'bold'), align='center')
    else:
        print('La turtle bleue a gagné !')
        print_winner(player2)

def print_winner(Turtle0):
    time.sleep(0.5)
    while True:
        set_turtle(painter, (0, screen_size_y / 4), color='#6600CC')
        painter.write(f"Le champion est le turtle {turtle_color[Turtle0]}", font=('ArcadeClassic', font_size*2, 'bold'), align='center')
        time.sleep(1.5)
        set_turtle(painter, (0, screen_size_y / 4), color='white')
        painter.write(f"Le champion est le turtle {turtle_color[Turtle0]}", font=('ArcadeClassic', font_size*2, 'bold'), align='center')
        time.sleep(1)
