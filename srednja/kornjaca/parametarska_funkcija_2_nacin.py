import math
import turtle
from turtle import *
from math import sin, cos


N = 750
SCALE_FACTOR = 125


def calculate_x(t):
    return math.pow(cos(t), 3)


def calculate_y(t):
    return math.pow(sin(t), 3)


turtle.pensize(2)
turtle.speed("fastest")
x0 = calculate_x(0)
y0 = calculate_y(0)
penup()
goto(x0 * SCALE_FACTOR, y0 * SCALE_FACTOR)
pendown()

for i in range(N):
    t = i / N * 2 * math.pi
    xi = calculate_x(t)
    yi = calculate_y(t)
    goto(xi * SCALE_FACTOR, yi * SCALE_FACTOR)

done()
