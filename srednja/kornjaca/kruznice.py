from turtle import *


def krug(r,x,y,boja):
    if r<5:
        return
    else:
        pu()
        goto(x,y)
        pd()
        color(boja, boja, boja)
        begin_fill()
        circle(r)
        end_fill()
        krug(r - 10, x, y + 10, boja + 0.1)


krug(200, 0, -100, 0)

done()
