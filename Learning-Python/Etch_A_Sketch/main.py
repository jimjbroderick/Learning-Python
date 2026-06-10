from turtle import Turtle, Screen

screen = Screen()
screen.listen()

etchy = Turtle()
etchy.shape("arrow")
etchy.color("green")

def clear_screen():
    etchy.clear()

def move_forward():
    etchy.forward(20)

def turn_left():
    etchy.left(5)

def turn_right():
    etchy.right(5)

def move_back():
    etchy.back(5)

screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=move_back, key="s")
screen.onkey(fun=clear_screen, key="c")






screen.exitonclick()