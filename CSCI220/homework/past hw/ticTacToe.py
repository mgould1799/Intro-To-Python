#Name:Meagan Gould
#Purpose: to create a tic tac toe game in idle
#Certification of Authenticity: I certify that this is my own work
#       I did talk to Eduardo, Stephanie, and Prof. Stalvey about this. 

def boardNums():
    nums=["1","2","3",
          "4","5","6",
          "7","8","9"]
    
    return nums
#input: list of numbers
#output: board display to use during tic tac toe
def boardDisplay(nums):
    print(nums[0],"|",nums[1],"|",nums[2])
    print("----------")
    print(nums[3],"|",nums[4],"|",nums[5])
    print("----------")
    print(nums[6],"|",nums[7],"|",nums[8])


#input:the entry to which the player wishes to place their X or O
#   the board numbers, and the X or O to be placed into that position
#Output: the list of numbers that are changed from numbers to x or o
#       in that position 
def fillBoard(entry,board,letter):
    board2=board
    if entry>=1 and entry<=9 and(letter=="X" or letter=="O"):
        pos=entry-1
        change=board2[pos]=letter
    

#input:numberList for tic tac toe board and entry from the user
#output: if a positon has been filled with x or o 
def usedOrNot(nums,entry):
    pos=entry-1
    
    if nums[pos]=="X" or nums[pos]=="O":
        used=True
    else:
        used=False
    return used


#input:number list
#output: positions to figure out if player has won or not
def wonOrNot(num):
    win=False
    #horizontal x wins
    if num[0]=="X" and num[1]=="X" and num[2]=="X":
        win=True
    elif num[3]=="X" and num[4]=="X" and num[5]=="X":
        win=True
    elif num[6]=="X" and num[7]=="X" and num[8]=="X":
        win=True
    #diagonal x wins
    elif num[0]=="X" and num[4]=="X" and num[8]=="X":
        win=True
    elif num[2]=="X" and num[4]=="X" and num[6]=="X":
        win=True
    #vertical x wins
    elif num[0]=="X" and num[3]=="X" and num[6]=="X":
        win=True
    elif num[2]=="X" and num[5]=="X" and num[8]=="X":
        win=True
    elif num[1]=="X" and num[4]=="X" and num[7]=="X":
        win=True
    #horizontal O wins
    elif num[0]=="O" and num[1]=="O" and num[2]=="O":
        win=True
    elif num[3]=="O" and num[4]=="O" and num[5]=="O":
        win=True
    elif num[6]=="O" and num[7]=="O" and num[8]=="O":
        win=True
    #diagonal O wins
    elif num[0]=="O" and num[4]=="O" and num[8]=="O":
        win=True
    elif num[2]=="O" and num[4]=="O" and num[6]=="O":
        win=True
    #vertical O wins
    elif num[0]=="O" and num[3]=="O" and num[6]=="O":
        win=True
    elif num[2]=="O" and num[5]=="O" and num[8]=="O":
        win=True
    elif num[1]=="O" and num[4]=="O" and num[7]=="O":
        win=True
    return win

##def over(nums,winOrNot):
##    if winOrNot==True:
##        result=True
##    else:
##        result=False
##    return result

#input:number list of the board and the how many tries are in the game
#ouput: if game has been won or has tied with the two players
def gameOver(nums,playTimes):

    #calls the previous function that deteremines a winner
    hasWon=wonOrNot(nums)
    #sets the game to not over automatically
    gameOver=False

    #if someone has won loop that means game is over
    if hasWon==True:
        gameOver=True
    #if statement that determines if the game was a draw or not
    if playTimes==0:
        gameOver=True
        
    return gameOver
    
    
    
        
        
        
    
        
def playGame(): 
    #sets up the board
    gameNumbers=boardNums()
    startBoard=boardDisplay(gameNumbers)
    print("we are going to play a game called tic tac toe.")

    #num of times to play
    triesToPlay=9

    #statements to keep while loop playing for game, player1, and player2
    player1=False
    player2=False
    play=True

    print()
    

    #while loop to play game
    while play!=False :

        #while loop for player 1
        while player1!=True and triesToPlay!=0:

            #enter position and positon for player 1
            placeHolder=eval(input("player 1, enter a place to put x: "))
            position="X"

            
            #determine if position is used or not to fill the board
            if usedOrNot(gameNumbers,placeHolder)==False:
                fillBoard(placeHolder,gameNumbers,position)
                newBoard=boardDisplay(gameNumbers)
                #turns player 1 loop off and player 2 on
                player1=True
                player2=False

                #keeps track of tries so you can get out of loop if needed
                triesToPlay-=1
                
             #tells someone if that loop has been used or not   
            else:
                print("that position has already been used")
            #if statement to figure out if player 1 has won
            #if wonOrNot(numberList)==True:
            if wonOrNot(gameNumbers)==True and triesToPlay!=0:
                print("player 1 has won.")
                play=False
                player2=True
                player1=True

        #while loop for player 2 to play
        while player2!=True and triesToPlay!=0:
            
            placeHolder=eval(input("player 2, enter a place to put O: "))
            position="O"
            
            #if statement to figure out if a place has been used so it can
            #   be used or not
            if usedOrNot(gameNumbers,placeHolder)==False:
                fillBoard(placeHolder,gameNumbers,position)
                newBoard=boardDisplay(gameNumbers)
                #turns player 1 back on and player 2 off
                player1=False
                player2=True

                #keep track of number of tries 
                triesToPlay-=1

                

            #statement to tell if a position has been used or not
            else:
                print("that position has been used")
            #statement to figure out if player 2 has won
            if wonOrNot(gameNumbers)==True and triesToPlay!=0:
                print("player 2 has won.")
                #turns play loop off and player 1 and 2 off
                play=False
                player1=True
                player2=True
        #tells if a game is a draw or not and turns play off
        if triesToPlay==0:
            print("the game was a draw")
            play=False

        
        
        

def main():
##    play=False
####    nums=boardNums()
####    print(nums)
####    board=boardDisplay(nums)
##    nums=boardNums()
##    board=boardDisplay(nums)
##    while play!=True:
####        nums=boardNums()
####        board=boardDisplay(nums)
##        
##        enter=eval(input("enter a space for the board: "))
##        
##        newBoard=fillBoard(enter,nums,"x")
##        board2=boardDisplay(nums)
##
##        
##        
##    print(nums)
##    board2=boardDisplay(nums)
##    #print(board)
##
    playGame()
    

main()
