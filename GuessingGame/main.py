import random


def guess():
    lowerBound = int(input("What do you want the lower bound to be? "))
    upperBound = int(input("What do you want the upper bound to be? "))

    numberToGuess = random.randint(lowerBound, upperBound)

    guessedNumber = int(input("What do you think the number is? "))

    while guessedNumber != numberToGuess:
        guessedNumber = int(input("Try again: "))

    print("That's the right answer!")

def guessComputer():
    numberOfGuesses = 0
    lowerBound = int(input("What do you want the lower bound to be? "))
    upperBound = int(input("What do you want the upper bound to be? "))

    numberToGuess = int(input("What number do you want the computer to guess? "))

    while numberToGuess < lowerBound or numberToGuess > upperBound:
        numberToGuess = int(input("What number do you want the computer to guess? "))

    guessedNumber = random.randint(lowerBound, upperBound)
    numberOfGuesses += 1
    numbersGuessed = [guessedNumber]

    # We want to keep track of what numbers the computer is guessing
    # This is so the computer does not guess a number it has already guessed
    while guessedNumber != numberToGuess:
        print("The computer guessed %d, but that was not the answer" %(guessedNumber))
        guessedNumber = random.randint(lowerBound, upperBound)
        while guessedNumber in numbersGuessed:
            guessedNumber = random.randint(lowerBound, upperBound)
        numberOfGuesses += 1
        numbersGuessed.append(guessedNumber)

    print("The computer guessed %d and that was the answer! It took %d guesses" % (guessedNumber, numberOfGuesses))

# Get the type of guessing game the user wants to play
command = ""
while command != "guess" and command != "computer guess":
    command = input("What kind of guessing game do you want to play? ")

if command == "guess":
    print("You want to guess the number")
    guess()

if command == "computer guess":
    print("You want the computer to guess the number")
    guessComputer()
