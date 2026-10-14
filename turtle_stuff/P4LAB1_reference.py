# P4LAB1_reference.py
# CTI 110 - P4LAB1 - Loop House (instructor reference)
# Name: Instructor
# Date: 2026-10-06
# Purpose: Draw a house and a star with turtle graphics and loops.
#
# Pseudocode:
#   Set up the window: size, title with my name, background color
#   Set up the turtle: shape, colors, pen size, speed
#   Move to the bottom-left corner of the house
#   Start the fill
#   Repeat 4 times (for loop): forward 200, turn left 90
#   End the fill
#   Move to the top-left corner of the square
#   Set the side counter to 0, start the fill
#   While the counter is less than 3: forward 200, turn left 120, add 1
#   End the fill
#   Move to the sky
#   Repeat 5 times (for loop): forward 80, turn left 144
#   Hide the turtle and keep the window open

import turtle

screen = turtle.Screen()
screen.setup(800, 600)
screen.title("P4LAB1 - Instructor Reference")
screen.bgcolor("midnightblue")

t = turtle.Turtle()
t.shape("turtle")
t.color("gold")
t.pencolor("white")
t.pensize(3)
t.speed(0)

# lines drawn = 4 (walls) + 3 (roof) + 5 (star) = 12

# Walls: for loop
t.penup()
t.goto(-100, -150)
t.pendown()
t.fillcolor("tan")
t.begin_fill()
for side in range(4):
    t.forward(200)
    t.left(90)
t.end_fill()

# Roof: while loop
t.penup()
t.goto(-100, 50)
t.pendown()
t.fillcolor("firebrick")
sides = 0
t.begin_fill()
while sides < 3:
    t.forward(200)
    t.left(120)
    sides = sides + 1
t.end_fill()

# Star: the same kind of loop as the walls. Only the turn changed: 90 -> 144.
t.penup()
t.goto(200, 180)
t.pendown()
t.fillcolor("gold")
t.begin_fill()
for point in range(5):
    t.forward(80)
    t.left(144)
t.end_fill()

t.hideturtle()
turtle.done()
