import tkinter as tk
import random
import time
import re

class NumberGuessingGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Number Guessing Game")
        self.geometry("500x500")
        self.configure(bg="#E6CCFF")

        self.number = random.randint(1, 10)
        self.number_of_guesses = 0
        self.game_over = False

        self.player_name_label = tk.Label(self, text="Hello, What's your name?", bg="#E6CCFF", font=("Helvetica", 14))
        self.player_name_label.pack(pady=10)

        self.player_name_var = tk.StringVar()
        self.player_name_entry = tk.Entry(self, textvariable=self.player_name_var, font=("Helvetica", 14))
        self.player_name_entry.pack()
        self.player_name_entry.config(validate="key", validatecommand=(self.register(self.validate_name), "%S"))

        self.guess_label = tk.Label(self, text="Guess a number between 1 and 10:", bg="#E6CCFF", font=("Helvetica", 14))
        self.guess_label.pack(pady=10)

        self.guess_entry = tk.Entry(self, font=("Helvetica", 14))
        self.guess_entry.pack()

        self.submit_button = tk.Button(self, text="Submit", command=self.check_guess, font=("Helvetica", 14))
        self.submit_button.pack(pady=10)

        self.message_label = tk.Label(self, text="", bg="#E6CCFF", font=("Helvetica", 14))
        self.message_label.pack(pady=10)

        self.remaining_guesses_label = tk.Label(self, text="", bg="#E6CCFF", font=("Helvetica", 14))
        self.remaining_guesses_label.pack(pady=10)

        self.play_again_button = tk.Button(self, text="Play Again", command=self.reset_game, font=("Helvetica", 14))

    def validate_name(self, char):
        if not char.isalpha():
            return False
        return True

    def check_guess(self):
        if self.game_over:
            return

        guess = self.guess_entry.get()
        if not guess.isdigit() or int(guess) < 1 or int(guess) > 10:
            self.message_label.config(text="Please enter a number between 1 and 10.", fg="red")
            self.after(6000, self.clear_message)
            return

        guess = int(guess)
        self.number_of_guesses += 1

        if guess < self.number:
            self.message_label.config(text="Your guess is too low.", fg="blue")
            self.after(6000, self.clear_message)
        elif guess > self.number:
            self.message_label.config(text="Your guess is too high.", fg="blue")
            self.after(6000, self.clear_message)
        else:
            self.message_label.config(text=f"Congratulations, {self.player_name_entry.get()}! "
                                             f"You guessed the number in {self.number_of_guesses} tries!", fg="green")
            self.play_again_button.pack(pady=10)
            self.submit_button.config(state=tk.DISABLED)
            self.game_over = True

        self.remaining_guesses_label.config(text=f"Remaining guesses: {5 - self.number_of_guesses}")

        if self.number_of_guesses == 5 and guess != self.number:
            self.message_label.config(text=f"Sorry, {self.player_name_entry.get()}, you did not guess the number. "
                                            f"The number was {self.number}", fg="red")
            self.play_again_button.pack(pady=10)
            self.submit_button.config(state=tk.DISABLED)
            self.game_over = True

    def clear_message(self):
        self.message_label.config(text="")

    def reset_game(self):
        self.number = random.randint(1, 10)
        self.number_of_guesses = 0
        self.remaining_guesses_label.config(text="")
        self.message_label.config(text="")
        self.play_again_button.pack_forget()
        self.submit_button.config(state=tk.NORMAL)
        self.game_over = False
        self.player_name_entry.delete(0, tk.END)


if __name__ == "__main__":
    app = NumberGuessingGame()
    app.mainloop()
