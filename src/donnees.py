""" We gather in this source file all different variables used during the game.

Author: Anthony
Version: 1.0
Date: 17.09.2015
Python: 2.7.10 64 bits """

# List with all the words of our database
words = list()

# Language used for the list of words (French by default).
language = str("french")

# Word to guess during the game
wordToGuess = str()

# Attempts left to guess the word (8 when beginning a new game)
attemptsLeft = int(8)

# List of tried letters by the player
triedLetters = list()

# Name of the player
playerName = str()

# Score of the player (0 if the player doesn't already exist)
playerScore = int()