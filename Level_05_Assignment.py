# Level #5 Assignment - Rock Paper Scissors
# IS 303 – Hilton
# Author: Caleb Nelson

import random

# Get a player choice and validate the result
def get_player_choice():
    while True:
        player_entry = input("Please type rock, paper, or scissors: ").lower()
        if player_entry in ["rock", "paper", "scissors"]:
            return player_entry
        else:
            print("Invalid entry.")

# Generate a choice for the computer
def get_computer_choice():
    computer_number = random.randint(1,3)
    if computer_number == 1:
        computer_entry = "rock"
    elif computer_number == 2:
        computer_entry = "paper"
    else: 
        computer_entry = "scissors"
    return computer_entry

# Determine the winner in a given round
def determine_winner(computer_entry, user_entry):
    if user_entry == computer_entry:
        return "tie"
    elif user_entry == "rock" and computer_entry == "scissors":
        return "win"
    elif user_entry == "scissors" and computer_entry == "paper":
        return "win"
    elif user_entry == "paper" and computer_entry == "rock":
        return "win"
    else:
        return "loss"

# Welcome the user to the game. 
print("Welcome to Python Rock Paper Scissors!")

# Ask them how many rounds they would like to play. 
while True:
    try:
        rounds = int(input("How many rounds would you like to play? (choose an odd number): "))

# Ensure that the number they enter is an odd number so there cannot be any ties.
        if rounds <= 0:
            print("Please enter a positive number.")
        elif rounds % 2 == 0:
            print("Please enter an odd number.")
        else:
            break

    except ValueError:
        print("Invalid input. Please enter a number.")

# Run through game play for the number of rounds chosen, keeping track of the number of wins/losses for both sides
player_win_count = 0
player_loss_count = 0
computer_win_count = 0
computer_loss_count = 0
round_count = 0

while round_count < rounds:
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    round_result = determine_winner(computer_choice, player_choice)
    # If it's a tie, the round doesn't count. Push through to the next one.
    print("------------------------")
    print("You: " + player_choice)
    print("Computer: " + computer_choice)

    if round_result == "tie":
        print("It's a tie. This round does not count. Try again.")
    elif round_result == "win":
        print("You win!")
        player_win_count += 1
        computer_loss_count += 1
        round_count += 1
    else:
        print("You lose.")
        player_loss_count += 1
        computer_win_count += 1
        round_count += 1

    print("------------------------")

# Determine the overall winner and print the results
if player_win_count > computer_win_count:
    print("------------------------")
    print("End tally:")
    print("Your wins: " + str(player_win_count))
    print("Computer wins: " + str(computer_win_count))
    print("You won! Congratulations! Thanks for playing!")
    print("------------------------")
elif player_win_count < computer_win_count:
    print("------------------------")
    print("End tally:")
    print("Your wins: " + str(player_win_count))
    print("Computer wins: " + str(computer_win_count))
    print("You lost. Sorry. Thanks for playing!")
    print("------------------------")
