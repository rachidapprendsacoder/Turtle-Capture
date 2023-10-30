from draw import window
from turtles import player1, player2, bot_player, player_color
from constants import map_size
from map_state import sq_list



def score():
    score_player = {player1: 0, player2: 0, bot_player: 0}

    for i in range(map_size[0]):
        for j in range(map_size[1]):
            if sq_list[i][j][2] == 4 * [player_color[player1]]: # si les quatre cotés du carré sont coloriés de la couleur de la turtle1
                score_player[player1] += 1
            elif sq_list[i][j][2] == 4 * [player_color[player2]]: # si les quatre cotés du carré sont coloriés de la couleur de la turtle1
                score_player[player2] += 1

    window.clearscreen()
    player1.write(f"J'ai un score de {score_player[player1]} pts", font=('Verdana', 40, 'normal'))
    player2.write(f"J'ai un score de {score_player[player2]} pts", font=('Verdana', 40, 'normal'))
    bot_player.write(f"J'ai un score de {score_player[bot_player]} pts", font=('Verdana', 40, 'normal'))
    print(f"la turtle rouge a un score de {score_player[player1]} pts")
    print(f"la turtle bleue a un score de {score_player[player2]} pts")
    print(f"la turtle verte a un score de {score_player[bot_player]} pts")

    if score_player[player1] > score_player[player2]:
        print('La turtle rouge a gagné !')
    elif score_player[player1] == score_player[player2]:
        print('Il y a égalité ! Les deux joueurs ont le même score !')
    else:
        print('La turtle bleue a gagné !')