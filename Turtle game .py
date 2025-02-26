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

"""
from turtle import *
from random import randint
import time

# Set dimensions for the race area
WIDTH, HEIGHT = 800, 600  # screen size
LANE_HEIGHT = 100  # Each racer's lane height
COLORS = ['black', 'purple', 'cyan', 'pink', 'brown']
start_pressed = False  # Flag to track if the race has started

def get_number_of_racers():
    # Asks user for number of racers (between 2 and 5)
    while True:
        racers = input("Enter the number of racers (2-5): ")
        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 5:
                return racers
        print("Invalid input! Please enter a number between 2 and 5.")

def start_race(x, y):
    #Function that starts the race when the button is clicked
    global start_pressed
    start_pressed = True
    start_button.clear()  # Remove button text
    start_button.hideturtle()  # Hide the button

def race(turtles):
    #Moves turtles forward randomly until one reaches the finish line.
    global start_pressed
    
    # Wait until the start button is clicked
    while not start_pressed:
        time.sleep(0.1)

    while True:
        for racer in turtles:
            distance = randint(1, 10)
            racer.forward(distance)

            if racer.xcor() >= WIDTH // 2 - 30:  # Finish line check
                declare_winner(racer)  # Show winner
                return racer.color()[0]

def declare_winner(winner_turtle):
    #Enlarges the winner and displays 'WINNER!' on the track.
    winner_turtle.shapesize(2)  # Double the size of the winner turtle

    # Display 'WINNER!' on the track
    winner_text = Turtle()
    winner_text.hideturtle()
    winner_text.penup()
    winner_text.goto(0, 0)  # Center the text
    winner_text.color("white")
    winner_text.write("WINNER!", align="center", font=("Arial", 36, "bold"))

def draw_track(num_racers):
    #Draws the racing track covering exactly where the turtles are placed.
    track_height = num_racers * LANE_HEIGHT  # Track height adjusts dynamically
    start_x = -WIDTH // 2  # Start of the track (left side)
    start_y = track_height // 2  # Center track on screen

    # Draw track background
    penup()
    goto(start_x, start_y)
    pendown()
    color("chocolate")
    begin_fill()
    for _ in range(2):
        forward(WIDTH)  # Full width of the screen
        right(90)
        forward(track_height)  # Track height based on number of racers
        right(90)
    end_fill()

    # Draw Finish Line
    penup()
    goto(WIDTH // 2 - 20, start_y)  # Position at the end of the track
    setheading(0)
    for i in range(num_racers):
        color("black" if i % 2 == 0 else "white")
        begin_fill()
        for _ in range(2):
            forward(20)
            right(90)
            forward(LANE_HEIGHT)
            right(90)
        end_fill()
        penup()
        goto(WIDTH // 2 - 20, start_y - (i + 1) * LANE_HEIGHT)
        pendown()
    
    penup()

def create_turtles(num_racers):
    #Creates and positions turtles at the start line.
    turtles = []
    start_x = -WIDTH // 2 + 30  
    track_height = num_racers * LANE_HEIGHT  # Track height based on racers
    start_y = track_height // 2 - LANE_HEIGHT // 2  # Center racers inside track

    for i in range(num_racers):
        racer = Turtle()
        racer.color(COLORS[i])
        racer.shape('turtle')
        racer.penup()

        # Position each racer inside its lane
        y_position = start_y - (i * LANE_HEIGHT)  
        racer.setpos(start_x, y_position)
        racer.pendown()
        turtles.append(racer)

    return turtles

def create_start_button():
    #Creates a clickable start button. 

    global start_button
    start_button = Turtle()
    start_button.penup()
    start_button.goto(0, -HEIGHT//2 + 50)  # Position at bottom center
    start_button.shape("square")
    start_button.color("black")
    start_button.shapesize(2, 6)  # Make the button wider
    start_button.showturtle()

    # Display text on the button
    start_button.write("START RACE", align="center", font=("Arial", 16, "bold"))

    # Make it clickable
    start_button.onclick(start_race)

def init_turtle():
    #Initializes the screen.
    screen = Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Race")
    screen.bgcolor("lightblue")

def main():
    racers = get_number_of_racers()
    init_turtle()
    draw_track(racers)  # Pass the number of racers to adjust track size
    turtles = create_turtles(racers)
    create_start_button()  # Add start button
    winner = race(turtles)
    print("The winner is the turtle with color:", winner)
    time.sleep(10)  
    done()

if __name__ == "__main__":
    main()
"""