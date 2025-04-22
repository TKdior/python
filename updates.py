import turtle
import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import time

# Constantes
WIDTH, HEIGHT = 800, 600
LANE_HEIGHT = 60
start_x = -WIDTH // 2 + 20
start_y = HEIGHT // 2 - 60
COLORS = ["red", "blue", "green", "orange", "purple", "yellow", "pink", "cyan"]

# Variables globales
screen = None
timer_display = None
turtles = []
num_racers = 5
race_running = False

# Fenêtre Tkinter
root = tk.Tk()
root.withdraw()  # Cacher au début

def get_number_of_racers():
    while True:
        num = simpledialog.askinteger("Nombre de joueurs", "Combien de joueurs (5-8) ?", minvalue=5, maxvalue=8)
        if num is None:
            return None
        if 5 <= num <= 8:
            return num
        else:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre entre 5 et 8.")

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

def draw_track(racers):
    track = turtle.Turtle()
    track.hideturtle()
    track.speed(0)
    for i in range(racers):
        track.penup()
        track.goto(start_x, start_y - (i * LANE_HEIGHT))
        track.pendown()
        track.forward(WIDTH - 40)

def create_turtles(racers):
    new_turtles = []
    for i in range(racers):
        racer = turtle.Turtle()
        racer.color(COLORS[i])
        racer.shape('turtle')
        racer.penup()
        racer.setpos(start_x, start_y - (i * LANE_HEIGHT))
        racer.pendown()
        new_turtles.append(racer)
    return new_turtles

def start_race():
    global race_running
    if race_running or not turtles:
        return

    race_running = True
    start_time = time.time()
    finished = False

    while not finished:
        for t in turtles:
            t.forward(random.randint(1, 5))
            if t.xcor() >= WIDTH // 2 - 20:
                finished = True
                winner = t.color()[0]
                break
        current_time = time.time() - start_time
        timer_display.clear()
        timer_display.write(f"Time: {current_time:.2f}s", align="center", font=("Arial", 24, "bold"))

    timer_display.clear()
    timer_display.write(f"{winner.capitalize()} wins! Time: {current_time:.2f}s", align="center", font=("Arial", 24, "bold"))
    race_running = False

def reset_race():
    global turtles, num_racers
    turtle.clearscreen()
    num = get_number_of_racers()
    if num:
        num_racers = num
        init_turtle()
        draw_track(num_racers)
        turtles.clear()
        turtles.extend(create_turtles(num_racers))

def exit_game():
    turtle.bye()
    root.quit()

def create_tkinter_buttons():
    root.title("Contrôles de la course")

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
    def main():
      global num_racers, turtles
      num = get_number_of_racers()
      if num:
        num_racers = num
        init_turtle()
        draw_track(num_racers)
        turtles.clear()
        turtles.extend(create_turtles(num_racers))
        create_tkinter_buttons()

    root.deiconify()
    root.mainloop()

if __name__ == "__main__":
    main()