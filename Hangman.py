import tkinter as tk
from PIL import ImageTk, Image

# Create the root window
root = tk.Tk()
root.title("Hangman")
root.geometry("450x400")

# Create a canvas for the hangman image
canvas = tk.Canvas(root, width=600, height=300)
canvas.pack()

# Create a list of image files for each stage of the hanging progression
# images = [tk.PhotoImage(file=f"hangman{i}.png") for i in range(7)]
images = [ImageTk.PhotoImage(Image.open(f"hangman{i}.png")) for i in range(7)]
canvas.create_image(200, 150, image=images[0])

# Create a label to display the word that the player is trying to guess
word_label = tk.Label(root, text="_ _ _ _ _", font=("Helvetica", 24))
word_label.pack()

# Create a frame for the letter buttons
frame = tk.Frame(root)
frame.pack(fill=tk.X)

# Global variables to keep track of the game state
word = "hello"
guesses = set()
stage = 0

# Function to guess a letter
def guess_letter(letter):
    global stage
    if letter in word:
        # Update the word label with the correct letter
        for i, c in enumerate(word):
            if c == letter:
                word_label.config(text=word_label.cget("text").replace("_", letter, 1))
        # Check if the player has won the game
        if "_" not in word_label.cget("text"):
            word_label.config(text="You won!")
            for button in frame.winfo_children():
                button.config(state=tk.DISABLED)
    else:
        # Increment the stage number and show the next stage of the hangman image
        stage += 1
        canvas.create_image(200, 150, image=images[stage])
        if stage == 6:
            # Game over
            word_label.config(text=f"The word was {word}.")
            for button in frame.winfo_children():
                button.config(state=tk.DISABLED)


# Create a button for each letter of the alphabet
for letter in "abcdefghijklmnopqrstuvwxyz":
    button = tk.Button(frame, text=letter, command=lambda l=letter: guess_letter(l))
    button.pack(side=tk.LEFT)

# Run the main loop
root.mainloop()
