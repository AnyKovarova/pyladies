import turtle
from random import randrange




def petal(turtle, radius, angle):
    for i in range(2):
        turtle.circle(radius, angle)
        turtle.left(180-angle)

def flower(turtle, n, radius, angle):
    for i in range(n):
        petal(turtle, radius, angle)
        turtle.left(360/n)

def draw(turtle, length):
    window = turtle.Screen()
    turtle.bgcolor('green')
    turtle.penup()
    turtle.forward(length)
    turtle.pendown()
    


num_flowers = 0
while num_flowers < 30:
    x = randrange(-400, 400)
    y = randrange(-400, 400)
    turtle.color('violet')
    turtle.speed(0)
    draw(turtle,150)
    turtle.begin_fill()
    flower(turtle,7,50,50)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    num_flowers +=1

exitonclick()