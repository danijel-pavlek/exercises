from turtle import *


RADIUS = 50
PENSIZE = 5

def draw_circle(center_x, center_y, circle_color, radius):
    penup()
    position_x = center_x - radius
    position_y = center_y - radius
    goto(position_x, position_y)
    color(circle_color)
    pendown()
    circle(radius)
    penup()


pensize(PENSIZE)
delta = 2 * (RADIUS + PENSIZE)
draw_circle(-100, 0, "blue", RADIUS)
draw_circle(-100 + delta, 0, "black", RADIUS)
draw_circle(-100 + 2 * delta, 0, "red", RADIUS)

draw_circle(-100 + delta/2, -delta/2, "yellow", RADIUS)
draw_circle(-100 + delta/2 + delta, -delta/2, "green", RADIUS)

done()
