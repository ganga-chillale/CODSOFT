import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("400x500")
        self.root.configure(bg="#282C34")  # Dark theme

        # Title Label
        self.title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 16, "bold"), fg="white", bg="#282C34")
        self.title_label.pack(pady=10)

        # Score Tracking
        self.user_score = 0
        self.computer_score = 0
        self.score_label = tk.Label(root, text="Your Score: 0  |  Computer Score: 0", font=("Arial", 12), fg="white", bg="#282C34")
        self.score_label.pack(pady=10)

        # Choices Display
        self.result_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 12), fg="white", bg="#282C34")
        self.result_label.pack(pady=10)

        # Buttons for User Choices
        self.rock_button = tk.Button(root, text="Rock", command=lambda: self.play("Rock"), bg="#61AFEF", fg="white", font=("Arial", 14), width=10)
        self.rock_button.pack(pady=5)

        self.paper_button = tk.Button(root, text="Paper", command=lambda: self.play("Paper"), bg="#98C379", fg="white", font=("Arial", 14), width=10)
        self.paper_button.pack(pady=5)

        self.scissors_button = tk.Button(root, text="Scissors", command=lambda: self.play("Scissors"), bg="#E06C75", fg="white", font=("Arial", 14), width=10)
        self.scissors_button.pack(pady=5)

        # Result Output
        self.user_choice_label = tk.Label(root, text="You Chose: ", font=("Arial", 12), fg="white", bg="#282C34")
        self.user_choice_label.pack(pady=5)

        self.computer_choice_label = tk.Label(root, text="Computer Chose: ", font=("Arial", 12), fg="white", bg="#282C34")
        self.computer_choice_label.pack(pady=5)

        self.final_result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="yellow", bg="#282C34")
        self.final_result_label.pack(pady=10)

        # Play Again Button
        self.play_again_button = tk.Button(root, text="Play Again", command=self.reset_game, bg="#C678DD", fg="white", font=("Arial", 12), width=12)
        self.play_again_button.pack(pady=5)

    def play(self, user_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        # Display Choices
        self.user_choice_label.config(text=f"You Chose: {user_choice}")
        self.computer_choice_label.config(text=f"Computer Chose: {computer_choice}")

        # Determine Winner
        if user_choice == computer_choice:
            result = "It's a Tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Scissors" and computer_choice == "Paper") or \
             (user_choice == "Paper" and computer_choice == "Rock"):
            result = "You Win! 🎉"
            self.user_score += 1
        else:
            result = "Computer Wins! 😢"
            self.computer_score += 1

        # Update Score
        self.score_label.config(text=f"Your Score: {self.user_score}  |  Computer Score: {self.computer_score}")
        self.final_result_label.config(text=result)

    def reset_game(self):
        self.user_choice_label.config(text="You Chose: ")
        self.computer_choice_label.config(text="Computer Chose: ")
        self.final_result_label.config(text="Choose Rock, Paper, or Scissors")

# Run Application
if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()
