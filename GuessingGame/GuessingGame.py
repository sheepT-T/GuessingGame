#Emilio Mercado
#CIS261 Guessing Game
import random
import sys

number = 0
numberGuessed = 0
counter = 0

def generate_number_to_be_guessed():
    global number
    number = random.randint(1, 100)

def display_welcome_message():
    print("Welcome to the Guess the Number Game")
    print("+++++++++++++++++++++++++++++++++++++")

def make_guess(guess_number):
    global numberGuessed, counter
    numberGuessed = guess_number
    counter += 1

def is_correct_guess():
    global numberGuessed, number
    return numberGuessed == number

def display_correct_guess_message():
    global counter
    print(f"Great work! You gussed it in {counter} tries.")

def display_please_guess_message():
    print("I'm thinking of a number between 1 and 100:")
    print("Try to guess it.")

def display_guess_again_message():
    global numberGuessed, number
    difference = numberGuessed - number
    if difference > 10:
        print("Way too high! Guess again.")
    elif difference <= 10 and difference > 0:
        print("Too high! Guess again.")
    elif difference < -10:
        print("Way too low! Guess again.")
    elif difference >= -10 and difference < 0:
        print("Too low. Guess again.")

def main():
    global guessNumber
    global counter
    guessNumber = 0
    play_again = "y"
    display_welcome_message()
    while play_again == "y":
        generate_number_to_be_guessed()
        display_please_guess_message()
        while guessNumber != number:
            print("Enter a number between 1 and 100: ")
            guessNumber = int(input())
            make_guess(guessNumber)
            if is_correct_guess():
                display_correct_guess_message()
                counter = 0
                break
            else:
                display_guess_again_message()
        play_again = input("Try Again? (y/n) ").lower()
        if play_again == "n":
            print("Bye - Come back soon!")
            sys.exit()

if __name__ == "__main__":
    main()
