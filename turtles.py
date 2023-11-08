import turtle as ttl
from constants import screen_size_x, path_size


builder = ttl.Turtle()
player1 = ttl.Turtle()
player2 = ttl.Turtle()
bot_player = ttl.Turtle()
deleter = ttl.Turtle()
painter = ttl.Turtle()
minute_timer = ttl.Turtle()
seconds_timer = ttl.Turtle()

turtle_color = {player1: 'red', player2: 'blue', bot_player: 'green'}

def set_turtle(turtle0, pos=(0, 0), hide=False, color=None, heading=0):
    turtle0.speed(0)  # supprime les animations des turtles
    if hide:
        turtle0.hideturtle()
    if color:
        turtle0.color(color)
        turtle0.fillcolor(color)
    turtle0.setheading(heading)
    turtle0.penup()
    turtle0.setpos(pos)
    turtle0.shape('turtle')
    turtle0.shapesize((3/3800)*screen_size_x)


set_turtle(builder, hide=True)
set_turtle(player1, (-5 * path_size, 0), color=turtle_color[player1])
set_turtle(player2, (5 * path_size, 0), color=turtle_color[player2], heading=180)
set_turtle(bot_player, color=turtle_color[bot_player], heading=90)
set_turtle(deleter, (-screen_size_x/2, 0), hide=True)
set_turtle(painter, hide=True)
set_turtle(minute_timer, (-path_size*1.5, path_size*1.5), color='white', heading=180)
set_turtle(seconds_timer, (path_size*1.5, path_size*1.5), color='white')


player_color = {player1: '#FF6721', player2: '#21baFF', bot_player: '#4AFF21', deleter: '#FEFEF1'}
speed = {player1: path_size / 2, player2: path_size / 2, bot_player: path_size / 2, deleter: path_size / 2}
