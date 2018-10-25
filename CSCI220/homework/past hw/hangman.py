#Name: Meagan Gould
#Hangman

import random

def readFile():
    infile=open("wordlist.txt","r")
    guessWord=[]
    for line in infile:
        word=line[:-1]
        guessWord.append(word)
    return guessWord

def randWord(wordList):
    
    ranNum=random.randint(0,len(wordList))
    word=wordList[ranNum]
    
    return word

def guessLetter(word):
    
    splitWord=word
    splitWordList=list(splitWord)
    guessWord=["_"]*len(word)
    correct=[] #list of guessed letters in the word
    wrong=[] #list of incorrect letters
    tries=0
   
    
    while  tries!=7 and guessWord!=splitWordList:
        
        
        
        guess=input("enter a letter to be guessed: ")
        if guess not in wrong and guess not in correct:
            for i in range(len(splitWordList)):
                if splitWordList[i]==guess:
                    guessWord.pop(i)
                    guessWord.insert(i,guess)
            try:
                guessIndex=splitWordList.index(guess)
                correct.append(guess)
            except ValueError:
                tries+=1
                wrong.append(guess)
                print("try again. that letter is not in there.")
            
                    
                               
##                    guessIndex=splitWordList.index(guess)
##                    guessWord.pop(guessIndex)
##                    guessWord.insert(guessIndex,guess)
##                correct.append(guess)
                
                
##            except ValueError:
##                tries+=1
##                wrong.append(guess)
##                print("try again. that letter is not in there.")
        else:
            print("you have already entered that letter. try again.")

        print()
        print("Correct guesses: ", correct)
        print("Wrong guesses: ",wrong)
        print(guessWord)
    guessWord=''.join(guessWord)

    return guessWord

def correct(word,guessWord):
    if word==guessWord:
        ans=True
    else:
        ans=False
    return ans

def gameIdle():
    print("let's play a game called hangman. you have 7 tries to guess the word")
    #wordList=readFile()
    #word=randWord(wordList)
    word = "omnipotence"
    print(word)
    guess=guessLetter(word)
    print()
    if correct(word,guess)==True:
        print("you have won the game.")
    else:
        print("you have lost the game. the word was: ",word)
    
        

def main():

##    wordList=readFile()
##    word=randWord(wordList)
##    print(word)
##    guessedWord = ["_"] * len(word)
##    print(guessedWord)
##    guess=guessLetter(word)
##    print(guess)
##    ans=correct(word,guess)
##    print(ans)
    gameIdle()

    

main()

                        
    
