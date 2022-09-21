import random

rsp = ["rock", "scissors", "paper"]
rsp_randomise = random.choice(rsp)
user_choice = input("Enter your choice: Rock, Scissors or Paper ")

if user_choice.lower() == rsp_randomise:
    print("Draw!")

elif user_choice.lower() == "rock":
    if rsp_randomise == "scissors":
        print("You win!")
    else:
        print("You lose(")

elif user_choice.lower() == "scissors":
    if rsp_randomise == "paper":
        print("You win!")
    else:
        print("You lose(")

elif user_choice.lower() == "paper":
    if rsp_randomise == "rock":
        print("You win")
    else:
        print("You lose(")

