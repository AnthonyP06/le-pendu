""" The hangman game. Run this file to play the game

Author: Anthony
Version: 1.0
Date: 18.09.2015
Python: 2.7.10 64 bits """

from fonctions import *
import donnees

# Choose a word (randomly) in the list of words.
donnees.wordToGuess = randomWord(donnees.words)

# Print the word to guess (only with stars '*' because the game has not began yet)
printWordToGuess(donnees.wordToGuess, donnees.triedLetters)

# Try letters whilst the player still has lives.
wordFound = False
while donnees.attemptsLeft > 0 and not wordFound:
	print "You have {} attempt(s) left.".format(donnees.attemptsLeft)
	
	# Suggest a letter
	letter = enterLetter()
	
	# Is this letter a good one?
	tryLetter(letter)
	
	# Print the word to guess
	printedWord = printWordToGuess(donnees.wordToGuess, donnees.triedLetters)
	
	# Is the word completely found?
	if str.find(printedWord, '*') == -1:
		wordFound = True

# Congrats!
print "Congratulations! You have found the word!"