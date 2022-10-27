from turtle import *


a = int(input("Unesite duljinu stranice a: "))
n = int(input("Unesite broj stranica: "))
delta = a * (1.0/n)
penup()
goto(0, 0)
pendown()


def draw_square_spiral(a):
    if a < 2:
        return
    setheading(0)
    forward(a)
    a -= delta / 4
    setheading(90)
    forward(a)
    a -= delta / 4
    setheading(180)
    forward(a)
    a -= delta / 4
    setheading(270)
    forward(a)
    a -= delta / 4
    draw_square_spiral(a)


draw_square_spiral(a)

done()
