""" Fonctions used for the game such as:
	* Relative to the hidden word
	* Relative to the database
	* Relative to the player and the score
	* Relative to the game itself

Author: Anthony
Version: 1.0
Date: 17.09.2015
Python: 2.7.10 64 bits """

import donnees

from random import randint

def getWords():
	""" Get the list of words from the database. If the file doesn't exist, the game ends and you are asked to check that your list actually exists in the repository './words'. Otherwise, create a list with either French words called 'french.txt' or English words called 'english.txt' and write down 1 word (in uppercases preferably) per line. """
	
	# Open the list of words (in mode "Reading only")
	listFile = open("./words/{}.txt".format(donnees.language), "r")
	
	# Add every word of the list file to the game list
	for word in listFile:
		donnees.words.append(word)
		
	# Close the open file
	listFile.close()
	
# ----------------------

def randomWord(wordsList):
	""" # Choose a word (randomly) from a list of words in order to play the game. If the list is empty, the game ends and you are asked to check that your list actually contains at least 1 word. """
	
	# Is the list empty?
	try:
		position = randint(0, len(wordsList)-1)
	except ValueError:
		print "The list of words is empty. Please check it and then reload the game."
		quit()
		
	# The list contains at least 1 word	
	return wordsList[position]
	
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

def enterLetter():
	""" Enter a single letter. It words with all a-z and A-Z letters. The game doesn't accept accentuated letters. If you try to enter any other char than allowed, you will be asked to try again with another one. """
	
	letter = str()
	
	# Enter a valid letter?
	letterValidity = False
	while not letterValidity:
		# Enter a single letter (automatically converted in upper letter)
		letter = raw_input("\n Please try a single letter : ").upper()
		
		# It is not a single letter
		if len(letter) != 1:
			print "It is not a single letter. You must enter a single letter."
			
		# Is the letter in the alphabet?
		if not letter.isalpha():
			print "This char is not in the alphabet. You must enter a letter."
			
		# Has the letter ever been suggested?
		if letter in donnees.triedLetters:
			print "You have already suggested this letter. Please try with another one."
	
		# The letter is valid
		if len(letter) == 1 and letter.isalpha() and letter not in donnees.triedLetters:
			letterValidity = True
	
	return letter
	
# ----------------------
	
def tryLetter(letter):
	""" Try a letter. If it is one letter matching with the hidden word, this letter appears to the player. The player has 1 attempt left otherwise. """
	
	# The letter is not a letter of the word to guess, 1 life less, nothing otherwise.
	if letter not in donnees.wordToGuess:
		donnees.attemptsLeft -= 1;
	
	# Add this letter to the list of suggested letters by the player
	donnees.triedLetters.append(letter)
# ----------------------

def printWordToGuess(word, triedLetters):
	""" Print the word to guess in uppercases, hiding the unfound letters and showing the guess ones. Hyphens are always printed. """
	
	# Strings are immutable, I'd better word with a list
	wordList = list(word.upper())
	
	# Has the letter been suggested by the player? If so, display the letter. Display a star '*' otherwise.
	for (position, letter) in enumerate(wordList):
		# Is the char a hyphen?
		if letter is "-":
			continue
		# Has the letter been tried? If no, keep hiding it.
		if letter not in triedLetters:
			wordList[position] = '*'
	
	# List to string
	wordPrinted = "".join(wordList)
	
	# Print the word
	print "\n ---> Word to guess : {} \n".format(wordPrinted)
	
	return wordPrinted