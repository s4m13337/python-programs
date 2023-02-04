#!/usr/bin/env python
import random

number = random.randint(1, 100)
tries = 1

print("Welcome to Guess the Number")
print("===========================")
print("I've thought of a number between 1 to 100. Try to guess it in as few tries as possible.")

guess = int(input("Your guess:\t"))

while(guess != number):
    if(guess < number):
        guess = int(input("Try guessing a higher number:\t"))
    else:
        guess = int(input("Try guessing a lower number:\t"))
    tries += 1

print("Congratulations! You guessed the number in {} tries. The number is {}".format(tries, number))
