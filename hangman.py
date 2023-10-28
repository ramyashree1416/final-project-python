import random
import tkinter as tk
from tkinter import messagebox

# List of words to choose from
word_list = ["python", "hangman", "computer", "programming", "openai", "coding"]

# Initialize global variables
chosen_word = ""
word_length = 0
guessed_letters = set()
attempts = 6

# Create the main game window
window = tk.Tk()
window.title("Hangman Game")

# Create and set up a gradient background
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()
canvas.create_rectangle(0, 0, 400, 400, fill="light blue", outline="light blue")
canvas.create_rectangle(0, 0, 400, 200, fill="light blue", outline="light blue")
canvas.create_rectangle(0, 200, 400, 400, fill="light yellow", outline="light yellow")

# Define custom button styles for a modern look
button_style = {
    "bg": "gray",
    "fg": "white",
    "activebackground": "dark gray",
    "activeforeground": "white",
    "font": ("Arial", 12),
}

# Create and set up the alphabet grid
alphabet_frame = tk.Frame(window, bg="light yellow")
alphabet_frame.pack()

for letter in "abcdefghijklmnopqrstuvwxyz":
    button = tk.Button(alphabet_frame, text=letter, width=2, command=lambda letter=letter: guess_letter(letter), **button_style)
    button.pack(side=tk.LEFT, padx=5, pady=5)

# Function to start a new game
def new_game():
    global chosen_word, word_length, guessed_letters, attempts

    # Reset game variables
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    guessed_letters = set()
    attempts = 6

    # Clear the canvas
    canvas.delete("all")

    # Display the current state of the word
    update_display()

# Function to make a guess
def guess_letter(letter):
    if letter not in guessed_letters:
        guessed_letters.add(letter)
        if letter not in chosen_word:
            draw_hangman()
        update_display()
        check_game_status()

# Function to update the word display
def update_display():
    display = ""
    for letter in chosen_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    display_word_label.config(text=display)

# Function to check if the game is won or lost
def check_game_status():
    if "_" not in display_word_label.cget("text"):
        messagebox.showinfo("Congratulations", "You guessed the word: " + chosen_word)
        new_game()
    elif attempts == 0:
        messagebox.showerror("Game Over", "You're out of attempts! The word was: " + chosen_word)
        new_game()

# Function to draw the hangman
def draw_hangman():
    global attempts
    if attempts == 6:
        canvas.create_oval(150, 50, 190, 90, width=2)
    elif attempts == 5:
        canvas.create_line(170, 90, 170, 200, width=2)
    elif attempts == 4:
        canvas.create_line(170, 100, 140, 150, width=2)
    elif attempts == 3:
        canvas.create_line(170, 100, 200, 150, width=2)
    elif attempts == 2:
        canvas.create_line(170, 200, 140, 250, width=2)
    elif attempts == 1:
        canvas.create_line(170, 200, 200, 250, width=2)
    attempts -= 1

# Create and configure the GUI elements
new_game_button = tk.Button(window, text="New Game", command=new_game, **button_style)
new_game_button.pack()

display_word_label = tk.Label(window, text="", font=("Arial", 16), bg="light yellow")
display_word_label.pack()

new_game()  # Start a new game when the program starts

# Start the main GUI loop
window.mainloop()
