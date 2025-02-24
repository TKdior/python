from turtle import *
from random import *
import turtle
import time
import random
import tkinter

WIDTH, HEIGHT = 500,500
COLORS = ['black','purple','cyan','pink','brown']


def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers(2-5): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric! Try again!")
            continue

        if 2<= racers <= 5:
            return racers
        else:
            print("Number is not in the range 2-5.")



def race(colors):
   turtles =  create_turtles(colors)
     

   while True:
       for racer in turtles:
           distance = random.randrange(1,30)
           racer.forward(distance)

           x,y = racer.pos()
           # passed the finish line
           if y >= HEIGHT//2 - 10:
               
               # accessing the color of the winner
               return colors[turtles.index(racer)]

def draw_track():
    goto(-350,200)
    pendown()
    color("chocolate")
    begin_fill()
    for i in range(2):
        forward(700)
        right(90)
        forward(400)
        right(90)
    end_fill()
    penup()
    goto(-WIDTH//2 - 10 ,HEIGHT//2  )
    pendown()
    # Finish line
    gap_size = 20
    shape("square")
    setheading(0)
    penup()

    # First white band
    color("white")
    for i in range(10):
        goto(250,(170 -(i*gap_size*2)))
        stamp()

    # Second white band
    color("white")
    for i in range(10):
        goto(250 + gap_size,((210 - gap_size) - (i*gap_size*2)))
        stamp()
    
    # First black band
    color("black")
    for i in range(10):
        goto(250,(190 -(i*gap_size*2)))
        stamp()

    # Second black band
    color("black")
    for i in range(10):
        goto(251 + gap_size,((190 - gap_size) - (i*gap_size*2)))
        stamp()
           

def create_turtles(colors):
    turtles = []
    spacingx = -WIDTH//(len(colors)+1)
    for i,color in enumerate(colors):
        racer= turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1)* spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def init_turtle():
  screen = turtle.Screen()
  screen.setup(WIDTH, HEIGHT)
  screen.title("MY FIRST RACERS GAME")
def main():
    racers = get_number_of_racers()
    init_turtle()
    draw_track()
    random.shuffle(COLORS)
    colors = COLORS[:racers]
    winner = race(colors)
    print("The winner is turtle the color:", winner)
    time.sleep(10)
    turtle.done()

if __name__ == "__main__":
    main()
tkinter.mainloop()
