# Hangman.py
# Name: Shefali Emmanuel
# CSCI 220 HW9
# Problem: To write a program to support the children's spelling game
#          hangman.
# Input:
# Output:      
# Certification of Authenticity:
# I certify that this lab is my own work, but I discussed it with:
# Eduardo.

#from graphics import*
import random

def hangman():
    infile = open("wordlist.txt","r")
    file_String = infile.read()
    return file_String.split()
    
def randomWord(fileList):
    word= fileList[random.randint(0, (len(fileList)-1))]
    return word

def guessed(word):
    length= len(word)
    guessList= []
    lettersGuessed = []
    wrongLettersGuessed= []
    for i in range(length):
        guessList.append("_")
    print(guessList)

    for i in range(7):
        coded= input("Enter a letter: ")
        lettersGuessed.append(coded)
        
        for j in range(word = guessList and i<7):
            if word[j] == coded:
                guessList[j] = coded
        
        for j in range(1):
            if word[j] != coded:
                print("Wrong Letter: " + str(coded))
                wrongLettersGuessed.append(coded)
                
            elif coded in wrongLettersGuessed:
                print("You Already Entered: " + str(coded))
                print("try again")
                        
        print(guessList)
        
def correctWord():
    if word == guessList:
        print("Correct!")

##def buildBlankWord():
##
##def playGame():
##    attempt=1
##    while attempt < len(word):
##        letter= ("Enter A Letter: ")
##        attempt += 1

def main():
    print("Let's play Hangman!")
    wordList = hangman()
    print(randomWord(wordList))
    guessed(randomWord(wordList))
    
main()
