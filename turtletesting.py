import turtle
import tkinter as tk

# Create a tkinter window
root = tk.Tk()
root.title("Turtle Graphics")
root.geometry("400x400")  # Set the window size

# Create a turtle screen
wn = turtle.Screen()
wn.bgcolor("darkred")

# Create a turtle
notta = turtle.Turtle()
notta.shape("turtle")
notta.pensize(3)

# Draw the clock hands
for viisari in range(12):
    notta.penup()
    notta.forward(180)
    notta.pendown()
    notta.forward(15)
    notta.penup()
    notta.forward(20)
    notta.stamp()
    notta.backward(215)
    notta.left(360/12)

wn.exitonclick()  # Close the turtle graphics window when clicked
