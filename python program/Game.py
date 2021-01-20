# Stone, Paper, Scissors Game
import random
user_action=input("Enter a choice(rock,paper,scissors):")
possible_action =["rock","paper","scissors"]
computer_action=random.choice(possible_action)
print(f"You chose {user_action} and computer use {computer_action}.")
if user_action == computer_action:
    print(f"Both Player selected {user_action}.It's a tie!")
elif user_action=="rock":
    if computer_action=="scissors":
        print("rock smashes scissors! you win")
    else:
        print("paper cover rock! you lose.")

elif user_action =="paper":
    if computer_action =="scissors":
        print("scissors cuts paper! you lose.")
    else:
        print("paper cover rock! you win")

elif user_action =="scissors":
    if computer_action=="paper":
        print("scissors cuts paper! you win")
    else:
        print("rock smashes scissors! you lose")