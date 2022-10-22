import turtle
from turtle import *


def draw_triangle_spirale(a):
    if a < 5:
        return
    else:
        turtle.setheading(0)
        turtle.forward(a)
        a -= 5
        turtle.setheading(120)
        turtle.forward(a)
        a -= 5
        turtle.setheading(240)
        turtle.forward(a)
        draw_triangle_spirale(a-5)


a = int(input("Unesite početnu duljinu stranice a: "))
turtle.setposition(0, 0)
draw_triangle_spirale(a)

done()
