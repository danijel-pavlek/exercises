from turtle import *


a = int(input("Unesite duljinu stranice a: "))
b = int(input("Unesite duljinu stranice b: "))

setheading(0)
forward(a)
setheading(90)
forward(b)
setheading(180)
forward(a)
setheading(270)
forward(b)

done()
