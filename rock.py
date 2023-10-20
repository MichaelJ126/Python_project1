# let's do it
import random

print("\tWelcome to to your demise. Here is where you skills will be tested with a simple game of Rock, Paper, Scissor. Can you best your opponenet? Take your chance player") 
start = input("Type 'start' to start the game or type 'quit' to quit game ")
while True:

    if start.lower() == "start":
     print("Game Started")
    cpu_options = ["rock", "paper", "scissors"]
    player_options = ["rock", "paper", "scissors"]

    player_input = input("Choose your weapon: 'rock', 'paper', or 'scissors' or 'quit'")
    if player_input.strip().lower() == 'rock': #if player typed in rock
        pOption = 'rock'


        def check_winner(option):
            if option.lower() == "rock" and random.choice(cpu_options) ==   "paper":
                print(f"You lose, CPU picked {random.choice(cpu_options)}" )
            elif option.lower() == "rock" and random.choice(cpu_options) == "rock":
                print("Tie")
            elif option.lower() == "rock" and random.choice(cpu_options) == "scissors":
                print("You win! FINALLY!")
        
            elif option.lower() == "paper" and random.choice(cpu_options) == "paper":
                print("Tie")
            elif option.lower() == "paper" and random.choice(cpu_options) == "rock":
                print("You win! FINALLY!")
            elif option.lower() == "paper" and random.choice(cpu_options) == "scissors":
                print(f"You lose, CPU picked {random.choice(cpu_options)}")
            elif option.lower() == "scissors" and random.choice(cpu_options) == "paper":
                print("You win! FINALLY!")
            elif option.lower() == "scissors" and random.choice(cpu_options) == "rock":
                print(f"You lose, CPU picked {random.choice(cpu_options)}")
            elif option.lower() == "scissors" and random.choice(cpu_options) == "scissors":
                print("Tie")
            elif option.lower() == "quit":
                break 
            else:
                print("Don't stir away from the game player, choose an option")
        check_winner(player_input)
    else:
        print("Thank you for playing!!! ")
        break




# if pOption.lower() == "rock" and random.choice(cpu_options) == "paper":
    #     print("You lose")
    # elif pOption.lower() == "rock" and random.choice(cpu_options) == "rock":
    #     print("Tie")
    # elif pOption.lower() == "rock" and random.choice(cpu_options) == "scissors":
    #     print("You win! FINALLY!")
