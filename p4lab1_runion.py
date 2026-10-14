# CTI 110
# P4LAB1 - Turtle
# runiona
# 10/6/2026

import turtle

screen = turtle.Screen()
screen.setup(800, 600)
screen.title("P4LAB1")
screen.bgcolor("DarkOrchid")

t= turtle.Turtle()

t.color("DarkGreen")
t.shape("turtle")
t.pencolor("DarkOrchid")
t.pensize(3)

"""
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
"""


sides = 4
angle = 360 / sides
length = 100
with t.fill():
    while sides > 0:
        t.forward(length)
        t.right(angle)
        sides = sides - 1
t.end_fill()

sides = 3
t.begin_fill()
t.fillcolor("gold")
for side in range(sides):
    t.forward(100)
    t.left(120)
t.end_fill()

t.teleport(-200,0)
sides = 4
t.begin_fill()
t.fillcolor("DarkGreen")
for side in range(sides):
    t.forward(length)
    t.right(angle)
t.end_fill()

sides = 3
t.begin_fill()
t.fillcolor("gold")
for side in range(sides):
    t.forward(100)
    t.left(120)
t.end_fill()
    
t.penup()
t.goto(200, 180)
t.pendown()

t.fillcolor("gold")
t.pencolor("gold")
t.begin_fill()
for point in range(5):
    t.forward(80)
    t.right(144)
t.end_fill()




turtle.done()