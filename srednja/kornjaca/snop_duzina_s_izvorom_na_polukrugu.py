import turtle
from turtle import *


n = int(input(" "))
r = 30
d = 150
delta = 15
for i in range(n):
    alpha = i/n * (180.0 - 2 * delta)
    setposition(0, 0)
    setheading(alpha+delta)
    turtle.up()
    forward(r)
    begin_poly()
    turtle.down()
    forward(d)
    turtle.up()
    end_poly()

setposition(0, 0)
setheading(90)
forward(100)
setheading(180)
forward(d / 2)
setheading(0)
turtle.down()
forward(d)
turtle.up()
setheading(270)
forward(15)
setheading(180)
turtle.down()
forward(d)


done()
