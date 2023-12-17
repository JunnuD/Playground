import turtle
import tkinter

wn = turtle.Screen()
wn.bgcolor("darkred")

notta = turtle.Turtle()
notta.shape("turtle")
notta.pensize(3)

for viisari in range (12):
    notta.penup()
    notta.forward(180)
    notta.pendown()
    notta.forward(15)
    notta.penup()
    notta.forward(20)
    notta.stamp()
    notta.backward(215)
    notta.left(360/12)

wn.mainloop()
