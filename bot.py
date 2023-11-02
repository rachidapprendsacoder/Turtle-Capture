from turtles import bot_player
import random
from move import move
from squares import center_square
from constants import map_size, sq_size
from map_state import sq_list

n_moves = 0
sqx, sqy = 0, 0

#le bot turtle choisi le carré vers lequel il va se diriger
def bot_choice_square():
    lign_sq_choice = random.randint(0, map_size[0])
    column_sq_choice = random.randint(0, map_size[1])
    return sq_list[lign_sq_choice-1][column_sq_choice-1][0]


def bot_turtle_movement():
    global n_moves
    global sqx, sqy
    tx, ty = bot_player.pos()
    n_moves += 1

    if n_moves % 17 == 0:
        sqx, sqy = center_square(bot_choice_square())  # change l'objet que va cibler le bot turtle

    if n_moves % 1 == 0:  # sert à régler la fréquence de déplacement du bot turtle
        if abs(sqx - tx) <= sq_size / 2 and abs(sqy - ty) <= sq_size / 2:  # si la turtle touche le carré
            sqx, sqy = center_square(bot_choice_square())  # change l'objet que va cibler le bot turtle
        else:  # si la tortue se situe à droite du carré et qu'elle est en dessous de celui-ci
            if sqx <= tx and ty <= sqy:
                dir_choice = random.choice(['up', 'left'])
                move(bot_player, dir_choice, 'bot')
            # Si la tortue se situe à gauche du carré et qu'elle est en dessous de celui-ci
            elif tx <= sqx and ty <= sqy:
                dir_choice = random.choice(['up', 'right'])
                move(bot_player, dir_choice, 'bot')
            # Si la tortue se situe à gauche du carré et qu'elle est au-dessus de celui-ci
            elif sqx <= tx and sqy <= ty:
                dir_choice = random.choice(['down', 'right'])
                move(bot_player, dir_choice, 'bot')
            # Si la tortue se situe à droite du carré et qu'elle est au-dessus de celui-ci
            elif tx <= sqx and sqy <= ty:
                dir_choice = random.choice(['down', 'left'])
                move(bot_player, dir_choice, 'bot')
