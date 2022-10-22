from turtle import *
from random import *


N = 7
SIZE = 200


def draw_horizontal_lines(n, starting_x, ending_x, starting_y, ending_y):
    current_y = starting_y
    step = (starting_y - ending_y) / (n-1)
    while current_y >= ending_y - pensize():
        penup()
        goto(starting_x, current_y)
        pendown()
        setheading(0)
        forward(ending_x - starting_x)
        current_y -= step


def draw_vertical_lines(n, starting_x, ending_x, starting_y, ending_y):
    current_x = starting_x
    step = (ending_x - starting_x) / (n-1)
    while current_x <= ending_x + pensize():
        penup()
        goto(current_x, starting_y)
        pendown()
        setheading(270)
        forward(starting_y - ending_y)
        current_x += step


def draw_random_lines(starting_column, starting_row, n_lines):
    current_column = starting_column
    current_row = starting_row
    step = SIZE / (n_lines - 1)
    x = -SIZE // 2 + step * starting_column
    y = SIZE // 2 - step * starting_row
    color("blue")
    while 0 < current_column < N - 1 and 0 < current_row < N - 1:
        penup()
        goto(x, y)
        angle = choice([0, 90, 180, 270])
        if angle == 0:
            current_column += 1
        elif angle == 180:
            current_column -= 1
        elif angle == 90:
            current_row -= 1
        elif angle == 270:
            current_row += 1
        setheading(angle)
        pendown()
        forward(step)
        x = -SIZE // 2 + step * current_column
        y = SIZE // 2 - step * current_row


pensize(5)
draw_horizontal_lines(N, -SIZE//2, SIZE//2, SIZE//2, -SIZE//2)
draw_vertical_lines(N, -SIZE//2, SIZE//2, SIZE//2, -SIZE//2)
draw_random_lines(2, 2, N)

done()
