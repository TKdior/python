import turtle
import time
import random
import tkinter as tk

# Constants
WIDTH, HEIGHT = 800, 600
LANE_HEIGHT = 100
COLORS = ['black', 'purple', 'cyan', 'pink', 'brown']
start_pressed = False
race_ongoing = False  # Track if a race has started

def get_number_of_racers():
    #Get number of racers from user input
    while True:
        racers = input("Enter the number of racers (2-5): ")
        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 5:
                return racers
        print("Invalid input! Please enter a number between 2 and 5.")

def start_race():
    #Starts the race when the button is clicked
    global start_pressed, race_ongoing
    start_pressed = True
    race_ongoing = True
    root.quit()

def reset_race():
    #Resets the race properly, keeping the window open
    global start_pressed
    start_pressed = False
    race_ongoing = False
    turtle.clearscreen()

    main ()

def exit_game():
    #Closes both Turtle and Tkinter windows properly
    root.destroy()  # Close Tkinter
    turtle.bye()  # Close Turtle window

def race():
    #Moves turtles randomly until one reaches the finish line
    global turtles
    while not start_pressed:
        time.sleep(0.1)  # Wait for start

    while True:
        for racer in turtles:
            racer.forward(random.randint(1, 10))
            if racer.xcor() >= WIDTH // 2 - 30:
                declare_winner(racer)
                return

def declare_winner(winner_turtle):
    #Displays the winner and enlarges the turtle
    winner_turtle.shapesize(2)

    # Winner text
    winner_text = turtle.Turtle()
    winner_text.hideturtle()
    winner_text.penup()
    winner_text.goto(0, 50)
    winner_text.color("white")
    winner_text.write("WINNER!", align="center", font=("Arial", 36, "bold"))

    # Color text
    color_name = winner_turtle.color()[0].capitalize()
    color_text = turtle.Turtle()
    color_text.hideturtle()
    color_text.penup()
    color_text.goto(0, -50)
    color_text.color("white")
    color_text.write(f"{color_name} Wins!", align="center", font=("Arial", 28, "bold"))

def draw_track(num_racers):
    #Draws the racing track dynamically based on racers, including the finish line
    track_height = num_racers * LANE_HEIGHT
    start_x = -WIDTH // 2
    start_y = track_height // 2
    finish_x = WIDTH // 2 - 30

    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.pendown()
    turtle.color("chocolate")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(WIDTH)
        turtle.right(90)
        turtle.forward(track_height)
        turtle.right(90)
    turtle.end_fill()

    # Draw finish line
    turtle.penup()
    turtle.goto(finish_x, start_y)
    for i in range(num_racers):
        turtle.color("black" if i % 2 == 0 else "white")
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(20)
            turtle.right(90)
            turtle.forward(LANE_HEIGHT)
            turtle.right(90)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(finish_x, start_y - (i + 1) * LANE_HEIGHT)

def create_turtles(num_racers):
    #Creates and positions turtles at the start line
    turtles = []
    start_x = -WIDTH // 2 + 30
    track_height = num_racers * LANE_HEIGHT
    start_y = track_height // 2 - LANE_HEIGHT // 2

    for i in range(num_racers):
        racer = turtle.Turtle()
        racer.color(COLORS[i])
        racer.shape('turtle')
        racer.penup()
        racer.setpos(start_x, start_y - (i * LANE_HEIGHT))
        racer.pendown()
        turtles.append(racer)

    return turtles

def init_turtle():
    # Initialize the screen
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Race")

    screen.bgpic("img.png")  # Background image

    return screen


def create_tkinter_buttons():
    #Creates Tkinter window with Start, Reset, and Exit buttons
    global root
    root = tk.Tk()
    root.title("Race Controls")

    # Start button
    start_button = tk.Button(root, text="Start Race", command=start_race,
                             font=("Arial", 16, "bold"), bg="green", fg="white",
                             padx=20, pady=10, cursor="hand2")
    start_button.pack(padx=20, pady=10)

    # Reset button
    reset_button = tk.Button(root, text="Reset Race", command=reset_race,
                             font=("Arial", 16, "bold"), bg="blue", fg="white",
                             padx=20, pady=10, cursor="hand2")
    reset_button.pack(padx=20, pady=10)

    # Exit button
    exit_button = tk.Button(root, text="Exit Game", command=exit_game,
                            font=("Arial", 16, "bold"), bg="red", fg="white",
                            padx=20, pady=10, cursor="hand2")
    exit_button.pack(padx=20, pady=10)

    root.mainloop()

def main():
    global turtles
    num_racers = get_number_of_racers()
    draw_track(num_racers)
    turtles = create_turtles(num_racers)
    
    create_tkinter_buttons()  # Wait for user input (start/reset/exit)
    
    race()
    time.sleep(20)

if __name__ == "__main__":
    main()