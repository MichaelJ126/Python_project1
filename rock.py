# let's do it
import random
cpu_options = ["rock", "paper", "scissor"]
player_options = ["rock", "paper", "scissor"]

def check_rock(option):
    if option.lower() == "rock" and random.choice(cpu_options) == "paper":
        print("You lose, CPU picked paper" )
    elif option.lower() == "rock" and random.choice(cpu_options) == "rock":
        print("Tie")
    else:
        print("You win! FINALLY!")

def check_paper(option):
    if option.lower() == "paper" and random.choice(cpu_options) == "paper":
        print("Tie")
    elif option.lower() == "paper" and random.choice(cpu_options) == "rock":
        print("You win! FINALLY!")

    else:
        print(f"You lose, CPU picked scissors")


def check_scissors(option):
    if option.lower() == "scissor" and random.choice(cpu_options) == "paper":
        print("You win! FINALLY!")

    elif option.lower() == "scissor" and random.choice(cpu_options) == "rock":
        print(f"You lose, CPU picked rock")
    else:

        print("Tie")

oBool = True

print("Welcome to to your demise. Here is where you skills will be tested with a simple game of Rock, Paper, Scissor. Can you best your opponenet? Take your chance player") 
start = input("Type 'start' to start the game or type 'quit' to quit game: ")
while oBool:
    if start.lower() == "start":
        print("\nGame Started")
        player_input = input("Choose your weapon: 'rock', 'paper', or 'scissor' or 'quit': ")
        if player_input.strip().lower() == 'rock':
            pOption = 'rock'
            check_rock(pOption)

        elif player_input.strip().lower() == 'paper':
            pOption = 'paper'
            check_paper(pOption)

        elif player_input.strip().lower() == 'scissor':
            pOption = 'scissor'
            check_scissors(pOption)
        elif player_input.strip().lower() == "quit":
            print("Thank you for playing!!! ")
            oBool = False
        else:
            print("Don't stir away from the game player, choose an option")
    else:
        print("Thank you for playing!!! ")
        break





# if pOption.lower() == "rock" and random.choice(cpu_options) == "paper":
    #     print("You lose")
    # elif pOption.lower() == "rock" and random.choice(cpu_options) == "rock":
    #     print("Tie")
    # elif pOption.lower() == "rock" and random.choice(cpu_options) == "scissors":
    #     print("You win! FINALLY!")
