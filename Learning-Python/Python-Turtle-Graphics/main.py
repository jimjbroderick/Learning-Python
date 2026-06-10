#import another_module
#print(another_module.another_variable)
import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)
def random_color():
    #colors = ["LawnGreen", "BlueViolet", "CornflowerBlue", "DeepPink", "cyan", "gold", "OrangeRed"]
    #color = random.choice(colors)
    #return color
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


def random_angle():
    angles = [90, 180, 270, 360]
    angle = random.choice(angles)
    return angle

def draw_shape(sides):
    color = random_color()
    timmy.color(color)
    timmy.width(12)
    angle = 360 / sides
    for n in range (0, sides):
        timmy.forward(100)
        timmy.right(angle)

timmy = Turtle()
timmy.penup()
timmy.shape("circle")
timmy.color("BlueViolet")
#timmy.width(12)
timmy.speed("fastest")
#tammy = Turtle()
#tammy.shape("circle")
timmy.setposition(0,0)
#print(timmy)
timmy.pendown()

#for d in range (3, 11):
#    draw_shape(d)

#for n in range(0, 50):
#    timmy.color(random_color())
#    timmy.forward(30)
#    timmy.right(random_angle())

for n in range (0, 360, 5):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.right(5)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
# table.align["Type"] = "c"
# print (table)