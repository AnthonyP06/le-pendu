""" The hangman game. Run this file to play the game

Author: Anthony
Version: 1.0
Date: 18.09.2015
Python: 2.7.10 64 bits """

from fonctions import *
import donnees

# Choose a word (randomly) in the list of words.
wordToGuess = randomWord(donnees.words)

# Print the word to guess (only with stars '*' because the game has not began yet)
printWordToGuess(wordToGuess, donnees.words)