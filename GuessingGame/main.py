import random


def guess():
    lowerBound = int(input("What do you want the lower bound to be? "))
    upperBound = int(input("What do you want the upper bound to be? "))

    numberToGuess = random.randint(lowerBound, upperBound)

    guessedNumber = int(input("What do you think the number is? "))

    while guessedNumber != numberToGuess:
        guessedNumber = int(input("Try again: "))

    print("That's the right answer!")


# Get the type of guessing game the user wants to play
command = ""
while command != "guess" and command != "computer guess":
    command = input("What kind of guessing game do you want to play? ")

if command == "guess":
    print("You want to guess the number")
    guess()

if command == "computer guess":
    print("You want the computer to guess the number")
