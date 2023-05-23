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



setup_score_turtle()
screen.mainloop()