import turtle  
import random  
import time  
import tkinter as tk  
from tkinter import messagebox  

# Constants
WIDTH, HEIGHT = 800, 600  
LANE_HEIGHT = 75  
COLORS = ['black', 'purple', 'cyan', 'pink', 'magenta', 'red', 'blue', 'orange']  

# Global Variables
start_pressed = False  
turtles = []  
screen = None  
racers = 0  
start_time = None  
finishers = []  
timer_display = None  

# GUI Variables
root = tk.Tk()
root.withdraw()

def get_number_of_racers():
    while True:
        try:
            racers = int(input("Enter the number of racers (5-8): "))
            if 5 <= racers <= 8:
                return racers
        except ValueError:
            pass
        print("Invalid input! Please enter a number between 5 and 8.")

def start_race():
    global start_pressed, start_time
    start_pressed = True
    start_time = time.time()
    root.quit()

def reset_race():
    global start_pressed, turtles, finishers
    start_pressed = False
    finishers.clear()
    turtle.clearscreen()
    draw_track(racers)
    turtles = create_turtles(racers)

def exit_game():
    turtle.bye()
    root.quit()
    root.destroy()

def race():
    global finishers
    while not start_pressed:
        time.sleep(0.1)

    while len(finishers) < 3 and len(finishers) < racers:  
        for racer in turtles:
            if racer not in [f[0] for f in finishers]:  
                racer.forward(random.randint(1, 10))
                if racer.xcor() >= WIDTH // 2 - 30:  
                    finish_time = round(time.time() - start_time, 2)  
                    finishers.append((racer, finish_time))  
                    update_timer_display(finish_time)  
                    if len(finishers) == min(3, racers):
                        declare_winners()
                        return  

def update_timer_display(current_time):
    timer_display.clear()
    timer_display.color("red")
    timer_display.write(f"Time: {current_time:.2f}s", align="center", font=("Arial", 24, "bold"))

def declare_winners():
    turtle.clearscreen()
    turtle.bgcolor("lightblue")

    winner_display = turtle.Turtle()
    winner_display.hideturtle()
    winner_display.penup()
    winner_display.goto(0, 100)
    winner_display.write("🏆 Race Results 🏆", align="center", font=("Arial", 36, "bold"))

    y_offset = 50
    for i, (turtle_obj, finish_time) in enumerate(finishers):
        color = turtle_obj.color()[0].capitalize()
        winner_display.goto(0, 100 - (i + 1) * y_offset)
        winner_display.write(f"{i+1}. {color} - {finish_time}s", align="center", font=("Arial", 28, "bold"))

    show_winner_menu()

def show_winner_menu():
    winner_message = "\n".join(
        [f"{i+1}. {turtle_obj.color()[0].capitalize()} - {finish_time}s" for i, (turtle_obj, finish_time) in enumerate(finishers)]
    )
    
    messagebox.showinfo("🏆 Race Results 🏆", f"{winner_message}\n\nClick OK to restart the race.")  
    reset_race()  

def draw_track(num_racers):
    track_height = num_racers * LANE_HEIGHT
    start_x = -WIDTH // 2
    finish_x = WIDTH // 2 - 30
    start_y = track_height // 2

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
    new_turtles = []
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
        new_turtles.append(racer)

    return new_turtles

def init_turtle():
    global screen, timer_display
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Race")

    try:
        screen.bgpic("im.png")
    except turtle.TurtleGraphicsError:
        screen.bgcolor("lightblue")

    timer_display = turtle.Turtle()
    timer_display.hideturtle()
    timer_display.penup()
    timer_display.goto(0, HEIGHT // 2 - 50)
    timer_display.color("red")
    timer_display.write("Time: 0.00s", align="center", font=("Arial", 24, "bold"))

def create_tkinter_buttons():
    global root
    root.deiconify()  
    root.title("Turtle Race Controls")
    
    start_button = tk.Button(root, text="Start Race", command=start_race,
                             font=("Arial", 16, "bold"), bg="green", fg="white",
                             padx=20, pady=10, cursor="hand2")
    start_button.pack(padx=20, pady=10)

    reset_button = tk.Button(root, text="Reset Race", command=reset_race,
                             font=("Arial", 16, "bold"), bg="blue", fg="white",
                             padx=20, pady=10, cursor="hand2")
    reset_button.pack(padx=20, pady=10)

    exit_button = tk.Button(root, text="Exit Game", command=exit_game,
                            font=("Arial", 16, "bold"), bg="red", fg="white",
                            padx=20, pady=10, cursor="hand2")
    exit_button.pack(padx=20, pady=10)

    root.mainloop()

def main():
    global racers, turtles
    racers = get_number_of_racers()
    init_turtle()
    draw_track(racers)
    turtles = create_turtles(racers)
    create_tkinter_buttons()
    race()
    time.sleep(5)
    turtle.done()

if __name__ == "__main__":
    main()