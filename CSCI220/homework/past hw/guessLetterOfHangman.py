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
            
        else:
            print("you have already entered that letter. try again.")

        print()
        print("Correct guesses: ", correct)
        print("Wrong guesses: ",wrong)
        print(guessWord)
    guessWord=''.join(guessWord)

    return guessWord
