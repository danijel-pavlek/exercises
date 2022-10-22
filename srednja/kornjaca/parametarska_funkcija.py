import turtle
from turtle import *
from math import sin, cos


# f(t)
# -------------
# x = cos(t+pi)
# y = sin(t+pi)

turtle.fillcolor(0.0, 0.7, 1.0)
turtle.pensize(5)

points = []
for t in range(600):
    ti = 3.1415 * 2 * t/600
    xi = cos(ti + 3.1415) * 50
    yi = sin(ti + 3.1415) * 50
    points.append((xi, yi))

turtle.speed("fastest")
turtle.begin_poly()
for i in range(9999):
    xi, yi = points[i]
    xj, yj = points[i+1]
    turtle.up()
    setposition(xi, yi)
    turtle.down()
    goto(xj, yj)
turtle.end_poly()

done()
