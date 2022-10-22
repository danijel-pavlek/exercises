from turtle import *


def square(a, b):
    setheading(0)
    setposition(0, 0)
    forward(a)
    setheading(90)
    forward(b)
    setheading(180)
    forward(a)
    setheading(270)
    forward(b)


a = int(input("Unesite duljinu stranice a: "))
b = int(input("Unesite duljinu stranice b: "))

square(a, b)

done()
