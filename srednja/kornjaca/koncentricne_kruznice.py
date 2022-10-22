from turtle import *


BRIGHTEN_COLOR_FACTOR = 0.9
RADIUS_DECREASE_VARIABLE = 25
INITIAL_RADIUS = 200


def concentric_circles(radius, circle_color, position_y):
    if radius < 5:
        return
    else:
        begin_fill()
        final_circle_color = 1 - circle_color * BRIGHTEN_COLOR_FACTOR
        fillcolor(final_circle_color, final_circle_color, final_circle_color)
        pendown()
        circle(radius)
        penup()
        end_fill()
    setposition(0, position_y + RADIUS_DECREASE_VARIABLE)
    concentric_circles(radius - RADIUS_DECREASE_VARIABLE,
                       circle_color * BRIGHTEN_COLOR_FACTOR,
                       position_y + RADIUS_DECREASE_VARIABLE)


concentric_circles(INITIAL_RADIUS, 1, 0)


done()
