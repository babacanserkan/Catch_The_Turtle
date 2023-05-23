import turtle

screen = turtle.Screen()
screen.title("Catch The Turtle")
FONT = ("arial", 25, "normal")

def setup_score_turtle():
    score_turtle = turtle.Turtle()
    score_turtle.hideturtle()
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.85

    score_turtle.goto(0, y)
    score_turtle.write("Score: 0", align="center", font=FONT)

grid_size = 10

def make_turtle(x, y):
    t = turtle.Turtle()

    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("dark green")
    t.goto(x * grid_size, y * grid_size)

x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10]

def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)


turtle.tracer(0)

setup_turtles()
setup_score_turtle()

turtle.tracer(1)

screen.mainloop()