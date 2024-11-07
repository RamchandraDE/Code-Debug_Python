"""
ROCK PAPER SCISSORS

"""

import random

options = ["rock", "paper", "scissor"]
computer_guess = random.choice(options)
user_guess = input("Enter rock/paper/scissors = ")

if user_guess == " rock" and computer_guess == " scissors":
    print("you won")
elif user_guess == "paper" and computer_guess == "rock":
    print("you won")
elif user_guess == "scissors" and computer_guess == "paper":
    print("you won")
elif user_guess == computer_guess:
    print("Tie")

else:
    print(f"You lost, cmputer guess was{computer_guess}")
