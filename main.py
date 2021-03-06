from random import *
import random
from art import logo
print(logo)

# My Solution

print("Welcome to the guessing game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
answer = ""

guesses_remaining = 0

rand_num = randint(1, 100)
print(f"Psst! The answer is {rand_num}")

if difficulty == "easy":
    guesses_remaining = 10
elif difficulty == "hard":
    guesses_remaining = 5

while guesses_remaining > 0:
    print(f"You have {guesses_remaining} more attempts to guess the right number.")
    guess = int(input("Make a guess: "))
    if guess > rand_num:
        print("Too high.")
        guesses_remaining -= 1 
        if guesses_remaining == 0:
            print("You've run out of guesses. You lose.")
        else:
            print("Guess again.")
    elif guess < rand_num:
        print("Too low.")
        guesses_remaining -= 1
        if guesses_remaining == 0:
            print("You've run out of guesses. You lose.")
        else:
            print("Guess again.")
    else:
        guesses_remaining = 0
        answer = "correct"

if guesses_remaining == 0:
    if answer == "correct":
        print(f"You got it! The answer is {rand_num}.")


                


    
    
