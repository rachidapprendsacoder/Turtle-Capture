from constants import map_size
from utils import column_pos, lign_pos


# Créé l'objet 'carré'
def create_square(pos, square, sides, corners):
    return [pos, square, sides, corners]


# Matrice des carrés
sq_list = [[0 for j in range(map_size[1])] for i in range(map_size[0])]
for i in range(map_size[0]):
    for j in range(map_size[1]):
        sq_list[i][j] = create_square([column_pos(j), lign_pos(i)], 'black', [0, 0, 0, 0], [0, 0, 0, 0])  # les 0 seront remplacés par la couleur qui aura capturé la zone
                                                                    # carré, [haut, bas, gauche, droite], [haut-gauche, haut-droit, bas-gauche, bas-droit]
        