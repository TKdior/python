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
           

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH//(len(colors)+1)
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

racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
print("The winner is turtle the color:",winner)
time.sleep(10)

turtle.done()
tkinter.mainloop()
