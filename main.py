import tkinter as tk
import time
import vlc
import threading
from PIL import Image, ImageTk

def play_background_music():
    player = vlc.MediaPlayer('Sacred Lotus - Patiño.mp3')
    player.play()

music_thread = threading.Thread(target=play_background_music)
music_thread.start()

points = 0

def add_points(number_of_points):
    global points
    points += number_of_points

def print_points():
    points_label.config(text="You have {} adventure points.".format(points))

def typewriter(text, text_widget):
    for letter in text:
        text_widget.config(state=tk.NORMAL)
        if letter == "\n":
            text_widget.insert(tk.END, "\n")
        else:
            text_widget.insert(tk.END, letter)
            text_widget.see(tk.END)
        text_widget.config(state=tk.DISABLED)
        text_widget.update()
        time.sleep(0.05)

def start_game():
    welcome_frame.pack_forget()
    name_frame.pack()

def submit_name():
    global points
    name = name_entry.get()
    add_points(10)
    print_points()
    typewriter(f"\n\n{name}, you stand at the base of Mount Everest, ready to begin your ascent!", output_text)
    name_frame.pack_forget()
    decision_frame.pack()

def make_decision(decision):
    if decision == "begin":
        typewriter("\n\nYou have decided to begin your climb!", output_text)
        add_points(10)
        print_points()
        typewriter("\nYou start your journey through the rugged terrain of the Khumbu Icefall.", output_text)
        typewriter("\nThe path is treacherous, and you must decide whether to cross a shaky ladder over a deep crevasse or take a longer, safer route around.", output_text)
        typewriter("\nWhich will you choose?", output_text)
        show_decision_image()
        decision_frame.pack_forget()
        route_frame.pack()
    elif decision == "prepare":
        add_points(5)
        print_points()
        typewriter("\nYou decide to spend more time preparing and checking your gear.", output_text)
        typewriter("\nThe weather looks clear, and you feel ready to tackle the climb.", output_text)
    elif decision == "rest":
        add_points(5)
        print_points()
        typewriter("\nYou decide to rest and gather strength for the climb.", output_text)
    else:
        typewriter("\nInvalid choice. Please select a valid option.", output_text)

def show_decision_image():
    image = Image.open("Capture.PNG")
    image = image.resize((400, 300))
    photo = ImageTk.PhotoImage(image)

    image_label.config(image=photo)
    image_label.image = photo

def choose_route(route):
    if route == "ladder":
        typewriter("\n\nYou bravely cross the shaky ladder!", output_text)
        add_points(30)
        print_points()
        typewriter("\nAs you carefully step, the ladder wobbles, but you make it to the other side safely.", output_text)
        typewriter("\nYour heart races, but you feel a sense of accomplishment.", output_text)
    elif route == "safe":
        add_points(20)
        print_points()
        typewriter("\nYou choose the safer route around the crevasse.", output_text)
        typewriter("\nThe path is longer, but you manage to avoid the dangers of the ladder.", output_text)
        typewriter("\nYou conserve energy for the higher altitudes ahead.", output_text)
    else:
        print_points()

window = tk.Tk()
window.title("Everest Climb Adventure")
window.geometry("600x500")
window.resizable(False, False)

welcome_frame = tk.Frame(window)
name_frame = tk.Frame(window)
decision_frame = tk.Frame(window)
route_frame = tk.Frame(window)

welcome_label = tk.Label(welcome_frame, text="Welcome to your Mount Everest Adventure!")
welcome_label.pack()
start_button = tk.Button(welcome_frame, text="Start Game", command=start_game, bg="lightblue")
start_button.pack()

name_label = tk.Label(name_frame, text="Enter your name, brave climber:")
name_label.pack()
name_entry = tk.Entry(name_frame)
name_entry.pack()
name_button = tk.Button(name_frame, text="Submit", command=submit_name, bg="lightblue")
name_button.pack()

decision_label = tk.Label(decision_frame, text="Do you want to begin your climb, prepare more, or rest?")
decision_label.pack()

begin_button = tk.Button(decision_frame, text="Begin Climb", command=lambda: make_decision("begin"), bg="lightgreen")
begin_button.pack()

prepare_button = tk.Button(decision_frame, text="Prepare Gear", command=lambda: make_decision("prepare"), bg="lightyellow")
prepare_button.pack()

rest_button = tk.Button(decision_frame, text="Rest", command=lambda: make_decision("rest"), bg="lightpink")
rest_button.pack()

route_label = tk.Label(route_frame, text="Choose your path: Cross the ladder or take the safer route?")
route_label.pack()

ladder_button = tk.Button(route_frame, text="Cross the Ladder", command=lambda: choose_route("ladder"), bg="lightgreen")
ladder_button.pack()

safe_button = tk.Button(route_frame, text="Take the Safe Route", command=lambda: choose_route("safe"), bg="lightyellow")
safe_button.pack()

image_label = tk.Label(window)
image_label.pack()

output_text = tk.Text(window, height=10, width=50, wrap=tk.WORD)
output_text.config(state=tk.DISABLED)
output_text.pack()

points_label = tk.Label(window, text="You have 0 adventure points.")
points_label.pack()

welcome_frame.pack()
window.mainloop()
