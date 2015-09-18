""" Fonctions used for the game such as:
	* Relative to the hidden word
	* Relative to the database
	* Relative to the player and the score
	* Relative to the game itself

Author: Anthony
Version: 1.0
Date: 17.09.2015
Python: 2.7.10 64 bits """

from donnes.py import *

# Get the list of words from the database
def getWords():
	return 0
	
# ----------------------

# Choose a word (randomly) from a list of words in order to play the game
def randomWord(wordsList):
	return 0
	
# ----------------------

# Ask the player to enter a name for the game.
def enterNamePlayer():
	return 0
	
# ----------------------

# Get the score of a player. If the player doesn't exist, a new player is created, the initial score is 0.
def getScorePlayer(name):
	return 0
	
# ----------------------

# Set the score of a player
def setScorePlayer(name):
	return 0
		
# ----------------------

# Save the score of the player in 'scores' output file
def saveScorePlayer(name):
	return 0
	
# ----------------------

# Try a letter. If it is one letter matching with the hidden word, this letter appears to the player.
def tryLetter(letter):
	return 0
	
# ----------------------

# Print the guess to guess, hiding the unfound letters and showing the guess ones.
def printUnknownWord(triedLetters):
	return 0