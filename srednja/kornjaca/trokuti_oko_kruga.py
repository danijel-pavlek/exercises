import math
from turtle import *
import math


def draw_triangle(a, center_x, center_y, angle):
    penup()
    v = a * math.cos(math.pi/6)
    goto(center_x, center_y)
    setheading(angle)
    forward(v/2)
    pendown()
    left(150)
    forward(a)
    left(120)
    forward(a)
    left(120)
    forward(a)


current_angle = 0
step = 20
while current_angle < 360:
    draw_triangle(100, -50, 0, current_angle)
    current_angle += step


done()
