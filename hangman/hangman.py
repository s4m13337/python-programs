#!/usr/bin/env python3
from art import hangman_art
import csv
import random

# Function to get words from external file
def getWords(filename):
	elements = []
	with open(filename, 'r') as csvfile: 
		csvreader = csv.reader(csvfile)
		for element in csvreader: 
			elements.append(element)
	return elements

# Intilizations
HANGMAN = hangman_art()
max_tries = len(HANGMAN) - 1
word = random.choice(getWords('words.csv'))[0]
wrong = 0
guess_so_far = "_"*len(word)
used = []

# Greetings
print("HANGMAN")
print("=======")
print("Welcome to Hangman game. Guess the all the letters or get hanged!")

while(wrong < max_tries and guess_so_far != word):
    
    # Print status
    print(HANGMAN[wrong])
    print("You've used the following letters:\t {}.".format(used))
    print("The word so far is {}.".format(guess_so_far))
    guess = input("Enter a letter:\t")
    
    # Check if letter is already guessed
    while guess in used:
        guess = input("You've already guessed this. Guess another letter:\t")
    
    # Append newly guessed letter to used
    used.append(guess)
    
    # Check guess
    if guess in word:
        print("Yes! {} is in the word!".format(guess))
        blanks = ""
        for i in range(len(word)):
            if(guess == word[i]):
                blanks += guess
            else:
                blanks += guess_so_far[i]
        guess_so_far = blanks
    else:
        print("Sorry! {} isn't in the word.".format(guess))
        wrong += 1

# Ending the game
if(wrong == max_tries):
    print(HANGMAN[wrong])
    print("You have been hanged! GAME OVER!")
else:
    print("Congratulations! You guessed it!")
print("The word was {}.".format(word))