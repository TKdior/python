from turtle import *
from random import *
import turtle
import time
import random
import tkinter

WIDTH, HEIGHT = 800, 400  # Adjusted width for horizontal racing
COLORS = ['black', 'purple', 'cyan', 'pink', 'brown']

def get_number_of_racers():
    while True:
        racers = input("Enter the number of racers (2-5): ")
        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 5:
                return racers
        print("Input is not valid! Please enter a number between 2 and 5.")

def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1, 10)  # Adjusted for horizontal movement
            racer.forward(distance)
            x, y = racer.pos()
            # Check if the racer crossed the finish line
            if x >= WIDTH // 2 - 20:  # Finish line condition
                return colors[turtles.index(racer)]

def draw_track():
    penup()
    goto(-WIDTH // 2, HEIGHT // 2 - 50)
    pendown()
    color("chocolate")
    begin_fill()
    for _ in range(2):
        forward(WIDTH)
        right(90)
        forward(100)
        right(90)
    end_fill()
    
    # Draw Finish Line
    penup()
    goto(WIDTH // 2 - 20, HEIGHT // 2 - 50)
    setheading(0)
    pendown()
    color("white")
    begin_fill()
    for _ in range(2):
        forward(20)
        right(90)
        forward(100)
        right(90)
    end_fill()
    penup()

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
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
    print("The winner is the turtle with color:", winner)
    time.sleep(10)
    turtle.done()
