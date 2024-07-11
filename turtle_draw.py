from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def turn_left():
    timmy.setheading(timmy.heading()+10)


def turn_right():
    timmy.setheading(timmy.heading() - 10)


def clr():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkey(move_forward, key="w")
screen.onkey(move_backward, key="s")
screen.onkey(turn_left, key="a")
screen.onkey(turn_right, key="d")
screen.onkey(clr, key="c")
screen.exitonclick()
