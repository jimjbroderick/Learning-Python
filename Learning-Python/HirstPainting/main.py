import colorgram
import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

colors = colorgram.extract('image.jpg', 20)
rgb_colors = []
for n in colors:
    rgb_colors.append(n.rgb)

my_screen = Screen()
x_position = my_screen.canvwidth - 50
y_position = my_screen.canvheight - 50

hirst = Turtle()
hirst.hideturtle()
hirst.penup()
hirst.speed("fastest")
hirst.setposition(- x_position,- y_position)
def draw_line():
    for y in range (1, 16):
        random_color = random.choice(rgb_colors)
        hirst.dot(20, random_color)
        hirst.forward(40)

def new_line_left():
    hirst.left(90)
    hirst.forward(40)
    hirst.left(90)

def new_line_right():
    hirst.right(90)
    hirst.forward(40)
    hirst.right(90)

for lines in range(1, 8):
    draw_line()
    hirst.back(40)
    new_line_left()
    draw_line()
    hirst.back(40)
    new_line_right()

my_screen.exitonclick()