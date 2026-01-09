k=20
from turtle import *
left(90)
pendown()
for i in (0, 2):
    forward(14*k)
    left(270)
    back(12*k)
    right(90)
penup()
forward(9*k); right(90); back(7*k); left(90)
pendown()
for i in (0, 2):
    forward(13*k)
    right(90)
    forward(6*k)
    right(90)
penup()
for x in range(-15*k, 10*k, k):
    for y in range(-5*k, 25*k, k):
        goto(x, y)
        dot(3, "red")
done()