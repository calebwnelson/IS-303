# Author: Caleb Nelson
# CA Python game in which the computer chooses a random number and the player tries to
# guess that number.

# Import the random module so that we can generate a random number for the player to guess. 
# Set starting values for the number of rounds and the desire to play. 
import random
number_of_rounds = 0
user_desire = ("Y")

# Start a while loop that will continue as long as the user desires to play.
while user_desire == "Y":
    secret_number = random.randint(1, 100)
    number_of_guesses = 0
    if number_of_rounds < 1:
        user_desire = input("Would you like to play a guessing game? (Y/N): ").upper()
    else:
        # Ask the user if they would like to play again.
        user_desire = input("Would you like to play again? (Y/N): ").upper()
    # If “Y” or “y”, then play again with a new
    # random number. If not, then allow the program to exit.
    if user_desire != "Y":
        print("Thanks for playing! Goodbye!")
        break
    
    # Ask the player to enter a guess
    user_guess = int(input("I'm thinking of a number between 1 and 100. Try and guess it: "))
    
    # Make sure that guess is a valid number between 1 and 100
    # Invalid guesses should not count toward the total.
    # Compare the guess with the secret number. 
    # If the guess is too low, tell the player to guess higher.
    # If the guess is too high, tell the player to guess lower.
    while user_guess != secret_number:
        if user_guess >= 1 and user_guess <= 100:
            number_of_guesses += 1
            if user_guess < secret_number:
                print("Your guess is too low. Guess higher.")
                user_guess = int(input("Try again: "))
            elif user_guess > secret_number:
                print("Your guess is too high. Guess lower.")
                user_guess = int(input("Try again: "))
        else:
            print("Invalid guess. Please enter a number between 1 and 100.")
            user_guess = int(input("Try again: "))
    
    # Add correct guesses to the total number of guesses.
    number_of_guesses += 1

    # Increment the number of rounds played.
    number_of_rounds += 1
    
    # Congratulate the player.Print the results. Let the user know how many guesses it took. 
    # Then print a message, depending on how they did.
    # • 3 tries or less: Amazing!
    # • 4-5 tries: Impressive!
    # • 6-7 tries: Good job!
    # • 8-9 tries: Took a little longer, but you got there!
    # • 10 or more tries: You need to lock in.
    if number_of_guesses <= 3:
        print("Congratualtions! You guessed the secret number in", number_of_guesses, "tries. " \
        "That's amazing!")
    elif number_of_guesses <= 5:
        print("Congratualtions! You guessed the secret number in", number_of_guesses, "tries. " \
        "That's impressive!")
    elif number_of_guesses <= 7:
        print("Congratualtions! You guessed the secret number in", number_of_guesses, "tries. " \
        "Good job!")
    elif number_of_guesses <= 9:
        print("Congratualtions! You guessed the secret number in", number_of_guesses, "tries. " \
        "You took a little longer, but you got there!")
    else:
        print("Congratualtions! You guessed the secret number in", number_of_guesses, "tries. " \
        "You got it eventually, but you need to lock in.")

    

