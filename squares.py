from constants import map_size, sq_size, path_size
from draw import draw_square, draw_area, draw_captured_square
from turtles import player_color, painter
from map_state import sq_list


def center_square(pos):
    return [pos[0] + sq_size / 2, pos[1] - sq_size / 2]

# colorie
def update_squares(turtle0, pos):
    tx, ty = pos
    for i in range(map_size[0]):
        for j in range(map_size[1]): # pour chaque carré
            sqx, sqy = center_square(sq_list[i][j][0])
            # on regarde la position de la tortue par rapport au centre du carré
            # si elle est au-dessus :
            if sq_size / 2 <= ty - sqy <= sq_size and -sq_size / 2 < tx - sqx < sq_size / 2 and not sq_list[i][j][2][0] == player_color[turtle0]:
                sq_list[i][j][2][0] = player_color[turtle0]
                draw_area(painter, (sqx, sqy + (sq_size + path_size) / 2), 'h', player_color[turtle0])
                draw_captured_square(i, j, turtle0)
            # si elle est en-dessous :
            elif -sq_size <= ty - sqy <= -sq_size / 2 and -sq_size / 2 < tx - sqx < sq_size / 2 and not sq_list[i][j][2][1] == player_color[turtle0]:
                sq_list[i][j][2][1] = player_color[turtle0]
                draw_area(painter, (sqx, sqy - (sq_size + path_size) / 2), 'h', player_color[turtle0])
                draw_captured_square(i, j, turtle0)
            # si elle est à gauche :
            elif -sq_size <= tx - sqx <= -sq_size / 2 and -sq_size / 2 < ty - sqy < sq_size / 2 and not sq_list[i][j][2][2] == player_color[turtle0]:
                sq_list[i][j][2][2] = player_color[turtle0]
                draw_area(painter, (sqx - (sq_size + path_size) / 2, sqy), 'v', player_color[turtle0])
                draw_captured_square(i, j, turtle0)
            # si elle est à droite :
            elif sq_size / 2 <= tx - sqx <= sq_size and -sq_size / 2 < ty - sqy < sq_size / 2 and not sq_list[i][j][2][3] == player_color[turtle0]:
                sq_list[i][j][2][3] = player_color[turtle0]
                draw_area(painter, (sqx + (sq_size + path_size) / 2, sqy), 'v', player_color[turtle0])
                draw_captured_square(i, j, turtle0)

            # si elle est dans le coin supérieur gauche :
            elif sqx - sq_size <= tx <= sqx - sq_size / 2 and sqy + sq_size / 2 <= ty <= sqy + sq_size and not sq_list[i][j][3][0] == player_color[turtle0]:
                sq_list[i][j][3][0] = player_color[turtle0]
                draw_square(painter, (sqx - sq_size / 2 - path_size, sqy + sq_size / 2 + path_size), player_color[turtle0], path_size)
            # si elle est dans le coin supérieur droit :
            elif sqx + sq_size / 2 <= tx <= sqx + sq_size and sqy + sq_size / 2 <= ty <= sqy + sq_size and not sq_list[i][j][3][1] == player_color[turtle0]:
                sq_list[i][j][3][1] = player_color[turtle0]
                draw_square(painter, (sqx + sq_size / 2, sqy + sq_size / 2 + path_size), player_color[turtle0], path_size)
                # si elle est en bas à gauche :
            elif sqx - sq_size <= tx <= sqx - sq_size / 2 and sqy - sq_size <= ty <= sqy - sq_size / 2 and not sq_list[i][j][3][2] == player_color[turtle0]:
                sq_list[i][j][3][2] = player_color[turtle0]
                draw_square(painter, (sqx - sq_size / 2 - path_size, sqy - sq_size / 2), player_color[turtle0], path_size)
            # si elle est en bas à droite :
            elif sqx + sq_size / 2 <= tx <= sqx + sq_size and sqy - sq_size <= ty <= sqy - sq_size / 2 and not sq_list[i][j][3][3] == player_color[turtle0]:
                sq_list[i][j][3][3] = player_color[turtle0]
                draw_square(painter, (sqx + sq_size / 2, sqy - sq_size / 2), player_color[turtle0], path_size)
