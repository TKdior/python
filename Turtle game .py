# Turtle game 

from turtle import *
from random import randint

title('My first game')
bgcolor('black')
pencolor('white')
speed(0)
penup()
goto(-140,140)

# Racing game track
for step in range(15):
    write(step,align='center')
    right(90)

    for num in range(8):
       penup()
       forward(10)
       penup()
       forward(10) 
    penup
    backward(160)
    left(90)
    forward(20)
hideturtle()

# First player
player1 = Turtle()
player1.color('PINK')
player1.shape('turtle')

# first player racing track
player1.penup()
player1.goto(-160,100)
player1.pendown()

# 360 degre turn
for turn in range(10):
    player1.right(36)

# Second player
player2 = Turtle()
player2.color('GRAY')
player2.shape('turtle')

# first player racing track
player2.penup()
player2.goto(-160,70)
player2.pendown()

# 360 degre turn
for turn in range(72):
    player2.left(5)

# tHIRD player
player3 = Turtle()
player3.color('BlUE')
player3.shape('turtle')

# third player racing track
player3.penup()
player3.goto(-160,40)
player3.pendown()

# 360 degre turn
for turn in range(60):
    player3.right(6)

# Fourth player
player4 = Turtle()
player4.color('BROWN')
player4.shape('turtle')

# first player racing track
player4.penup()
player4.goto(-160,10)
player4.pendown()

# 360 degre turn
for turn in range(30):
    player4.right(12)

# turtles run at a random speed
for turn in range(100):
    player1.fd(randint(1,5))
    player2.fd(randint(1.5))
    player3.fd(randint(1.5))
    player4.fd(randint(1.5))

done()  