import turtle
from turtle import *
from math import sin


a = float(input("Učitaj koeficijent A: "))
b = float(input("Učitaj koeficijent B: "))
c = float(input("Učitaj koeficijent C: "))
d = float(input("Učitaj koeficijent D: "))

points = []
for x in range(600):
    xi = x - 300
    yi = a * sin(b*xi/50 + c) + d
    yi *= 50
    points.append((xi, yi))

turtle.speed("fastest")
turtle.begin_poly()
for i in range(599):
    xi, yi = points[i]
    xj, yj = points[i+1]
    turtle.up()
    setposition(xi, yi)
    turtle.down()
    goto(xj, yj)
turtle.end_poly()

done()
