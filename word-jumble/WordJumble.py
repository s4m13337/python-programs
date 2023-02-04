# Word jumble
# The computer picks a random word and jumbles it
# The player has to guess the correct word

import random
import csv
import sys

# define function to get words from external file
def getWords(filename):
	elements = []
	with open(filename, 'r') as csvfile: 
		csvreader = csv.reader(csvfile)
		for element in csvreader: 
			elements.append(element)
	return elements

# define function to jumble the word
def jumble(word):
	char = list(word)
	random.shuffle(char)
	jumbledWord = ""
	jumbledWord = jumbledWord.join(char)
	return jumbledWord

def main():
	
	# pick one word randomly from the sequence
	word = random.choice(WORDS)[0]

	# create a variable to store correct answer
	answer = word

	# create variable to store jumbled word
	jumbledWord = jumble(word)
	
	# access global variables trial and score
	global trial, score, playAgain

	print("The jumbled word is:\t{}".format(jumbledWord))
	userAnswer = input("Enter your answer:\t")
	while(userAnswer != answer and trial > 0) :
		print("Sorry, that is not the right word. Tries left:\t{}".format(trial))
		trial -= 1
		userAnswer = input("Enter your answer:\t")
	if trial == 0:
		print("----------------------------------------------------")
		print("GAME OVER! You have exhausted all your tries.")
		print("The correct answer was {}.".format(answer))
		print("----------------------------------------------------")
		print("Your score is:\t{}".format(score))
		print("----------------------------------------------------")
		playAgain = input('Would you like to play again? y/n:\t')
		print("----------------------------------------------------")
		trial = 2
		score = 0
	else:
		score += 1
		trial = 2
		print("Congratulations! {} is the correct answer." .format(answer))
		print("Your score is {}." .format(score))
		print("----------------------------------------------------")

# get a sequence of words to choose from
WORDS = getWords('Words.csv')

#variables to track trial and score
trial = 2
score = 0
playAgain = ''
print("----------------------------------------------------")
print("| ~~~~~~~ JumbleWord game (Created by Sam) ~~~~~~~ |")
print("----------------------------------------------------")

while(playAgain != 'n'):
	main()
	
sys.exit()
