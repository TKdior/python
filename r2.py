import turtle  # Import turtle graphics library
import random  # Import random module for random number generation
import time  # Import time module for sleep function
import tkinter as tk  # Import tkinter for GUI

# Constants
WIDTH, HEIGHT = 800, 600  # Screen width and height
LANE_HEIGHT = 100  # Height of each lane
COLORS = ['black', 'purple', 'cyan', 'pink', 'magenta']  # Colors for turtles
start_pressed = False  # Flag to check if start button is pressed
turtles = []  # List to store turtle objects
screen = None  # Variable to store turtle screen
racers = 0  # Variable to store number of racers

def get_number_of_racers():
    # Get number of racers from user input
    while True:
        racers = input("Enter the number of racers (2-5): ")  # Prompt user for input
        if racers.isdigit():  # Check if input is a digit
            racers = int(racers)  # Convert input to integer
            if 2 <= racers <= 5:  # Check if input is within valid range
                return racers  # Return number of racers
        print("Invalid input! Please enter a number between 2 and 5.")  # Print error message

def start_race():
    # Starts the race when the button is clicked
    global start_pressed  # Access global variable
    start_pressed = True  # Set start_pressed to True
    root.quit()  # Quit the tkinter main loop

def reset_race():
    # Resets the race without closing Tkinter
    global start_pressed, turtles  # Access global variables
    start_pressed = False  # Reset start_pressed to False
    turtle.clearscreen()  # Clear race track and turtles
    draw_track(racers)  # Redraw the track
    turtles = create_turtles(racers)  # Recreate turtles

def exit_game():
    # Exits the game
    turtle.bye()  # Close turtle graphics
    root.quit()  # Quit the tkinter main loop
    root.destroy()  # Destroy the tkinter window

def race():
    # Moves turtles randomly until one reaches the finish line
    global start_pressed  # Access global variable
    while not start_pressed:  # Wait for start button to be pressed
        time.sleep(0.1)  # Sleep for a short duration

    while True:  # Infinite loop to move turtles
        for racer in turtles:  # Iterate over each turtle
            racer.forward(random.randint(1, 10))  # Move turtle forward by a random distance
            if racer.xcor() >= WIDTH // 2 - 30:  # Check if turtle has reached the finish line
                declare_winner(racer)  # Declare the winner
                return racer.color()[0]  # Return the color of the winning turtle

def declare_winner(winner_turtle):
    # Displays winner's color name and doubles the turtle's size
    winner_turtle.shapesize(2)  # Double the size of the winning turtle

    winner_text = turtle.Turtle()  # Create a new turtle for displaying text
    winner_text.hideturtle()  # Hide the turtle
    winner_text.penup()  # Lift the pen up
    winner_text.goto(0, 50)  # Move to the specified position
    winner_text.color("white")  # Set text color to white
    winner_text.write("WINNER!", align="center", font=("Arial", 36, "bold"))  # Write "WINNER!" text

    color_name = winner_turtle.color()[0].capitalize()  # Get the color name of the winning turtle
    color_text = turtle.Turtle()  # Create another turtle for displaying color name
    color_text.hideturtle()  # Hide the turtle
    color_text.penup()  # Lift the pen up
    color_text.goto(0, -50)  # Move to the specified position
    color_text.color("black")  # Set text color to black
    color_text.write(f"{color_name} Wins!", align="center", font=("Arial", 28, "bold"))  # Write color name

def draw_track(num_racers):
    """Draws the racing track dynamically based on racers."""
    track_height = num_racers * LANE_HEIGHT  # Calculate track height
    start_x = -WIDTH // 2  # Starting x-coordinate
    finish_x = WIDTH // 2 - 30  # Finish line x-coordinate
    start_y = track_height // 2  # Starting y-coordinate

    turtle.penup()  # Lift the pen up
    turtle.goto(start_x, start_y)  # Move to the starting position
    turtle.pendown()  # Put the pen down
    turtle.color("chocolate")  # Set color to chocolate
    turtle.begin_fill()  # Begin filling the shape
    for _ in range(2):  # Draw the track rectangle
        turtle.forward(WIDTH)  # Move forward by width
        turtle.right(90)  # Turn right by 90 degrees
        turtle.forward(track_height)  # Move forward by track height
        turtle.right(90)  # Turn right by 90 degrees
    turtle.end_fill()  # End filling the shape

    # Draw finish line
    turtle.penup()  # Lift the pen up
    turtle.goto(finish_x, start_y)  # Move to the finish line position
    for i in range(num_racers):  # Draw finish line for each lane
        turtle.color("black" if i % 2 == 0 else "white")  # Alternate colors
        turtle.begin_fill()  # Begin filling the shape
        for _ in range(2):  # Draw the finish line rectangle
            turtle.forward(20)  # Move forward by 20 units
            turtle.right(90)  # Turn right by 90 degrees
            turtle.forward(LANE_HEIGHT)  # Move forward by lane height
            turtle.right(90)  # Turn right by 90 degrees
        turtle.end_fill()  # End filling the shape
        turtle.penup()  # Lift the pen up
        turtle.goto(finish_x, start_y - (i + 1) * LANE_HEIGHT)  # Move to the next lane

def create_turtles(num_racers):
    """Creates and positions turtles at the start line."""
    new_turtles = []  # List to store new turtles
    start_x = -WIDTH // 2 + 30  # Starting x-coordinate
    track_height = num_racers * LANE_HEIGHT  # Calculate track height
    start_y = track_height // 2 - LANE_HEIGHT // 2  # Starting y-coordinate

    for i in range(num_racers):  # Create turtles for each racer
        racer = turtle.Turtle()  # Create a new turtle
        racer.color(COLORS[i])  # Set turtle color
        racer.shape('turtle')  # Set turtle shape
        racer.penup()  # Lift the pen up
        racer.setpos(start_x, start_y - (i * LANE_HEIGHT))  # Position the turtle
        racer.pendown()  # Put the pen down
        new_turtles.append(racer)  # Add turtle to the list

    return new_turtles  # Return the list of turtles

def init_turtle():
    """Initializes the Turtle screen."""
    global screen  # Access global variable
    screen = turtle.Screen()  # Create a new turtle screen
    screen.setup(WIDTH, HEIGHT)  # Set up the screen size
    screen.title("Turtle Race")  # Set the screen title

    try:
        screen.bgpic("im.png")  # Set background image
    except turtle.TurtleGraphicsError:
        screen.bgcolor("lightblue")  # Set background color if image not found

def create_tkinter_buttons():
    """Creates a Tkinter window with Start, Reset, and Exit buttons."""
    global root  # Access global variable
    root = tk.Tk()  # Create a new tkinter window
    root.title("Turtle Race Controls")  # Set window title
    
    start_button = tk.Button(root, text="Start Race", command=start_race,
                             font=("Arial", 16, "bold"), bg="green", fg="white",
                             padx=20, pady=10, cursor="hand2")  # Create start button
    start_button.pack(padx=20, pady=10)  # Pack the button with padding

    reset_button = tk.Button(root, text="Reset Race", command=reset_race,
                             font=("Arial", 16, "bold"), bg="blue", fg="white",
                             padx=20, pady=10, cursor="hand2")  # Create reset button
    reset_button.pack(padx=20, pady=10)  # Pack the button with padding

    exit_button = tk.Button(root, text="Exit Game", command=exit_game,
                            font=("Arial", 16, "bold"), bg="red", fg="white",
                            padx=20, pady=10, cursor="hand2")  # Create exit button
    exit_button.pack(padx=20, pady=10)  # Pack the button with padding

    root.mainloop()  # Start the tkinter main loop

def main():
    global racers, turtles  # Access global variables
    racers = get_number_of_racers()  # Get number of racers from user
    init_turtle()  # Initialize turtle screen
    draw_track(racers)  # Draw the track
    turtles = create_turtles(racers)  # Create turtles
    create_tkinter_buttons()  # Create tkinter buttons
    winner = race()  # Start the race and get the winner
    print("The winner is the turtle with color:", winner)  # Print the winner
    time.sleep(5)  # Sleep for 5 seconds
    turtle.done()  # Close the turtle graphics window

if __name__ == "__main__":
    main()  # Call the main function