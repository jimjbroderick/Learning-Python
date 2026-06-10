from turtle import Turtle, Screen
from random import randint

ypos = [-100, -70, -40, -10, 20, 50]
turtle_colors = ["red", "blue", "green", "purple", "yellow", "orange"]

identifiers = []

for turtle_index in range(0, 6):
    tim = Turtle()
    tim.shape("turtle")
    tim.penup()
    tim.color(turtle_colors[turtle_index])
    tim.goto(x=-230, y = ypos[turtle_index])
    identifiers.append(tim)

finishline = 200
def race():
    race_ongoing = True
    while race_ongoing == True:
        for i in identifiers:
            randforward = randint(1, 20)
            i.forward(randforward)
            if i.xcor() >= finishline:
                print(f"The {i.pencolor()} turtle is the winner!")
                race_ongoing = False
                if user_bet == i.pencolor():
                    print("Your bet won!")
                else:
                    print("Your bet did not win.")

screen = Screen()
screen.setup(width=500, height=400)
#screen.listen()
user_bet = screen.textinput("Welcome to the Turtle Grand Prix!",
                            "Place your bet - pick a color!")

race()

#screen.onkey(fun=race, key="r")
screen.exitonclick()
