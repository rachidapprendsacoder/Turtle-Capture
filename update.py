from turtles import *
from draw import window, draw_circle_power
from bot import bot_turtle_movement
from carles import *
from score import score
from map_state import sq_list

events_appeared = {'speed_boost': 0}
event_taken = {'speed_boost': 0}
pos_events = {'speed_boost': 0}

current_duration = game_duration

def update_move(player, dir):
    print_timer()
    events(player)
    bot_turtle_movement()
    end_game()
    return move(player, dir)


def events(player):
    global events_appeared

    if timer() % 35 == 0 and timer() != 0:
        carles_apparition()

    if timer() == 20 and events_appeared['speed_boost'] == event_taken['speed_boost']: # si son heure est venue d'apparaître et si tous les speed_boost apparus n'ont pas encore été pris
        pos_events['speed_boost'] = speed_boost()  # le speed_boost apparait, on garde en mémoire sa position
        events_appeared['speed_boost'] += 1
    if events_appeared['speed_boost'] != event_taken['speed_boost']:  # s'il reste encore un speed_boost dans la map :
        speed_boost_take(player)


def speed_boost_take(player):
    tx, ty = player.pos()
    d = ((tx - pos_events['speed_boost'][0]) ** 2 + (ty - pos_events['speed_boost'][1]) ** 2)**0.5  # distance entre la tortue et le speed_boost
    if d <= path_size/2: # si la tortue se situe dans le cercle de centre speed_boost_pos et de rayon path_size / 2 :
        event_taken['speed_boost'] += 1
        draw_circle_power(pos_events['speed_boost'], player_color[player])
        speed[player] = path_size

def speed_boost():
    # lieu d'apparition
    lign_choice = random.randint(0, map_size[0])
    column_choice = random.randint(0, map_size[1])

    pos = (column_pos(column_choice), lign_pos(lign_choice) + path_size / 2)
    draw_circle_power(pos, 'red')
    return pos


def timer():
    return int(start_time + game_duration - time.time())


def print_timer():
    global current_duration

    if current_duration == timer():
        return
    else:
        minute_timer.color(sq_list[1][2][1])
        seconds_timer.color(sq_list[1][3][1])
        minute_timer.write(f"{current_duration // 60}min", font=('Verdana', 40, 'normal'), align='center')
        seconds_timer.write(f"{current_duration % 60}s", font=('Verdana', 40, 'normal'), align='center')
    minute_timer.color('white')
    seconds_timer.color('white')
    minute_timer.write(f"{timer()//60}min", font=('Verdana', 40, 'normal'), align='center')
    seconds_timer.write(f"{timer()%60}s", font=('Verdana', 40, 'normal'), align='center')
    current_duration = timer()

    window.title(f'Turtle Capture ({timer()}s)')

def end_game():
    if int(timer()) <= 0:  # Arrête la partie si le temps de jeu a été dépassé
        window.title('Turtle Capture')
        score()


window.listen()  # Active la détection des touches
window.onkey(lambda: update_move(player1, "up"), 'z')
window.onkey(lambda: update_move(player1, "down"), 's')
window.onkey(lambda: update_move(player1, "left"), 'q')
window.onkey(lambda: update_move(player1, "right"), 'd')
window.onkey(lambda: update_move(player2, "up"), 'Up')
window.onkey(lambda: update_move(player2, "down"), 'Down')
window.onkey(lambda: update_move(player2, "left"), 'Left')
window.onkey(lambda: update_move(player2, "right"), 'Right')