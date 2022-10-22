import turtle
from turtle import *


def square(x1, y1, a, boja):
    turtle.up()
    setposition(x1, y1)
    setheading(90)
    turtle.fillcolor(boja, boja, boja)
    turtle.down()
    begin_fill()
    forward(a)
    setheading(180)
    forward(a)
    setheading(270)
    forward(a)
    setheading(0)
    forward(a)
    end_fill()
    turtle.up()


a = int(input("Unesite duljinu stranice a: "))
n_squares_so_far = 0
x0, y0 = 100, 0
for i in range(7):
    yi = y0 + i * a
    for j in range(7):
        n_squares_so_far += 1
        xi = x0 + j * a
        square(xi, yi, a, n_squares_so_far/49.0)

done()
