#Name: Meagan Gould
#purpose: a program to play hangman in idle and graphics window
#input:a list to create the secret word to be guessed. letters entered by the
#       the user to guess the word
#output:the secret word,letters guessed, drawn hangman all to idle or the
#       graphics window that is created
#Certification of Authenticity: I certify that this is my own work
#       I did talk to Eduardo and Prof. Stalvey



import random
from graphics import *


#read's the text file for the secret word
def readFile():
    infile=open("wordlist.txt","r")
    guessWord=[]
    for line in infile:
        word=line[:-1]
        guessWord.append(word)
    return guessWord

#retrieves a random word from that list 
def randWord(wordList):
    
    ranNum=random.randint(0,len(wordList))
    word=wordList[ranNum]
    
    return word

#main function to guess a letter for the secret word
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

#function to tell if guess word actually matches the real word
def correct(word,guessWord):
    if word==guessWord:
        ans=True
    else:
        ans=False
    return ans


#function to play hangman in idle 
def gameIdle():
    print("let's play a game called hangman. you have 7 tries to guess the word")
    wordList=readFile()
    word=randWord(wordList)
    #word = "omnipotence"
    print(word)
    guess=guessLetter(word)
    print()
    if correct(word,guess)==True:
        print("you have won the game.")
    else:
        print("you have lost the game. the word was: ",word)


#function to tell if a box was clicked or not in the graphics window
        #it accepts a point and a rect tangle to check and returns
        #true if it was clicked
def wasClicked(pt,rect):
    if pt==None:
        returnVal= False
    else:
        rectP1=rect.getP1()
        rP1X=rectP1.getX()
        rP1Y=rectP1.getY()
    
        rectP2=rect.getP2()
        rP2X=rectP2.getX()
        rP2Y=rectP2.getY()

        ptX=pt.getX()
        ptY=pt.getY() 

        returnVal=ptX >= rP1X and ptX <= rP2X and ptY >= rP1Y and ptY <= rP2Y
    return returnVal


def gameWindow(word):
    #creates graph
    win=GraphWin("hangman",600,600)
    win.setBackground("white")

    

    #creates entry box
    entryPoint=Point(300,400)
    entryBox=Entry(entryPoint,5)
    entryBox.draw(win)

    

    #creates the basic hangman set up
    basePt1=Point(330,350)
    basePt2=Point(550,350)
    base=Line(basePt1,basePt2)
    base.draw(win)
    base.setFill("black")
    polePt1=Point(440,350)
    polePt2=Point(440,90)
    pole=Line(polePt1,polePt2)
    pole.draw(win)
    pole.setFill("black")
    extensionPt1=Point(440,90)
    extensionPt2=Point(330,90)
    extension=Line(extensionPt1,extensionPt2)
    extension.draw(win)
    extension.setFill("black")

    #creates hangman body
    headPt=Point(330,120)
    head=Circle(headPt,30)
    #head.draw(win)
    #head.setOutline("black")
    bodyPt1=Point(330,150)
    bodyPt2=Point(330,250)
    body=Line(bodyPt1,bodyPt2)
    #body.draw(win)
    #body.setFill("black")
    arm1=Line(Point(330,170),Point(360,170))
    #arm1.draw(win)
    #arm1.setFill("black")
    arm2=Line(Point(330,170),Point(300,170))
    #arm2.draw(win)
    #arm2.setFill("black")
    leg1=Line(Point(330,250),Point(360,275))
    #leg1.draw(win)
    #leg1.setFill("black")
    leg2=Line(Point(330,250),Point(300,275))
    #leg2.draw(win)
    #leg2.setFill("black")
    eye1=Point(320,115)
    eye2=Point(340,115)

    #creates the string for the secrect word
    guessWord=len(word)*["_"]
    guessWordText=Text(Point(300,500),guessWord)
    guessWordText.draw(win)

    ##creates the correct guess text box
    correct=[]
    correctText=Text(Point(100,460),correct)
    correctText.draw(win)
    correctText2=Text(Point(100,430),"Correct Guesses")
    correctText2.draw(win)

    ##creates the incorrect guess text box
    wrong=[]
    wrongText=Text(Point(500,460),wrong)
    wrongText.draw(win)
    wrongText2=Text(Point(500,430),"Incorrect Guesses")
    wrongText2.draw(win)

    ##creates the area for how many times are left in the game
    tries=7
    triesLeft=Text(Point(340,560),tries)
    triesLeft.draw(win)
    triesText=Text(Point(290,560),"Tries left: ")
    triesText.draw(win)

    #creates area to tell you have already entered that letter or
    #       or that letter is not in there
    errorText=Text(Point(300,540),"")
    errorText.draw(win)

    #won or lost text
    winOrLoseText=Text(Point(300,520),"")
    winOrLoseText.draw(win)

    ##creates the hangman game in the graphics window
    splitWord=word  #the acutual word
    splitWordList=list(splitWord) #splitting the word into a list 

    #yes and no box
    yesBox=Rectangle(Point(50,470),Point(100,520))
    noBox=Rectangle(Point(450,470),Point(500,520))
    yesText=Text(Point(75,490),"yes")
    noText=Text(Point(475,490),"no")

    #true or false statments(booleans) to get hangman to draw and play game
    #   over again
    play=False
    head_1=False
    body_1=False
    arm1_1=False
    arm2_1=False
    leg1_1=False
    leg2_1=False
    eye1_1=False
    eye2_1=False
    

    win.checkMouse()
    #loop to get game to play again
    while play!=True:

        #loop to figure out letters in the word
        while tries!=0 and guessWord!=splitWordList:
            win.getMouse()
            guess=entryBox.getText()
            
            if guess not in wrong and guess not in correct:
                for i in range(len(splitWordList)):
                    if splitWordList[i]==guess:
                        guessWord.pop(i)
                        guessWord.insert(i,guess)
                        guessWordText.setText(guessWord)
                        errorText.setText("")
                try:
                    guessIndex=splitWordList.index(guess)
                    correct.append(guess)
                    correctText.setText(correct)
                except ValueError:
                    tries-=1
                    wrong.append(guess)
                    wrongText.setText(wrong)
                    triesLeft.setText(tries)
                    errorText.setText("that letter is not in there")

                #if statements to get hangman to draw
                if tries ==6 and head_1==False:
                    head.draw(win)
                    head_1=True
                elif tries==5 and body_1==False:
                    body.draw(win)
                    body_1=True
                elif tries==4 and arm1_1==False:
                    arm1.draw(win)
                    arm1_1=True
                elif tries==3 and arm2_1==False:
                    arm2.draw(win)
                    arm2_1=True
                elif tries==2 and leg1_1==False:
                    leg1.draw(win)
                    leg1_1==True
                elif tries==1 and leg2_1==False:
                    leg2.draw(win)
                    leg2_1=True
                elif tries==0 and eye1_1==False and eye2_1==False:
                    eye1.draw(win)
                    eye2.draw(win)
                    eye1_1=True
                    eye2_1=True
                    
            #statement to say you have already entered that letter       
            else:
                errorText.setText("you have already entered that letter")

         
        #statement to say you have won the game or lost
        if splitWordList==guessWord:
           winOrLoseText.setText("you have won the game")
        if tries==0:
           winOrLoseText.setText("you have lost the game")

        #statement to get loop to run again
        if splitWordList==guessWord or tries==0:
            errorText.setText("would you like to play again?")
            yesBox.draw(win)
            noBox.draw(win)
            yesText.draw(win)
            noText.draw(win)
            pt=win.getMouse()
            if wasClicked(pt,yesBox)==True:
                main()
            if wasClicked(pt,noBox)==True:
                play=True
            
        
        
    win.getMouse()
    win.close()
    

    
    
    
        

def main():

    wordList=readFile()
    word=randWord(wordList)
    print(word)
##    guessedWord = ["_"] * len(word)
##    print(guessedWord)
##    guess=guessLetter(word)
##    print(guess)
##    ans=correct(word,guess)
##    print(ans)
    #gameIdle()
    gameWindow(word)

    

main()

                        
    
