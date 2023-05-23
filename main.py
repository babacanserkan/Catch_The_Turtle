import turtle
import random

screen = turtle.Screen()
screen.title("Catch The Turtle")
FONT = ("arial", 20, "normal")
score = 0
game_over = False

#turtle list
turtle_list = []

#score turtle
score_turtle = turtle.Turtle()

#countdown turtle
countdown_turtle = turtle.Turtle()

#make turtle propoerties
x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10]
grid_size = 10


def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.85
    score_turtle.setposition(0, y)
    score_turtle.write("Score: 0", align="center", font=FONT)


def make_turtle(x, y):
    t = turtle.Turtle()
    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(f"Score: {score}", align="center", font=FONT)

    t.onclick(handle_click)

    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("dark green")
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t)

def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.85
    countdown_turtle.setposition(0, y - 30)
    countdown_turtle.clear()


    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(f"Time: {time}", align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)

    else:
        game_over = True
        countdown_turtle.clear()
        countdown_turtle.write("Game Over!", align="center", font=FONT)

def start_game_up():
    turtle.tracer(0)

    setup_turtles()
    hide_turtles()
    setup_score_turtle()
    show_turtles_randomly()
    countdown(10)
    turtle.tracer(1)


start_game_up()
screen.mainloop()