# let's do it
import random

print("Welcome") 
start = input("Type 'start' to start the game or type 'quit' to quit game ")
if start.lower() == "start":
    print("Game Started")
else:
    print("Quitted Game")

cpu_options = ["rock", "paper", "scissors"]
player_options = ["rock", "paper", "scissors"]

player_input = input("Choose your weapon: 'rock', 'paper', or 'scissors' ")
if player_input.strip().lower() == 'rock': #if player typed in rock
        pOption = 'rock'

if pOption.lower() == "rock" and random.choice(cpu_options) == "paper":
    print("You lose")
elif pOption.lower() == "rock" and random.choice(cpu_options) == "rock":
    print("Tie")
elif pOption.lower() == "rock" and random.choice(cpu_options) == "scissors":
    print("You win! FINALLY!")

