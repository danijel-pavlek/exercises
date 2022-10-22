import math
from turtle import *


def draw_squares(position_x, position_y, a, angle):
    angle = angle % 360
    if a < 5:
        return
    else:
        penup()
        goto(position_x, position_y)
        pendown()
        setheading(angle)
        forward(a)
        setheading((angle + 90) % 360)
        forward(a)
        setheading((angle + 180) % 360)
        forward(a)
        setheading((angle + 270) % 360)
        forward(a)
        k = math.sqrt(2) / 2
        setheading(angle)
        if angle == 0:
            draw_squares(position_x + a / 2, position_y, a * k, 45)
        else:
            draw_squares(position_x - a * k / 2, position_y + a * k / 2, a * k, 0)


a = int(input("Unesite duljinu stranice a: "))
draw_squares(-250, -250, a, 0)

done()
