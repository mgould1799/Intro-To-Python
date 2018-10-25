##directionay works like a dictanary off the shelf. has a key that tells you info
##list are muitable


import random

##list=3,'a',4,'a','a',5
#find positon for 1,3,4 for the posistion of a
#def findInList(values):
    

def main():
    values =[]
    for i in range(10):
        values.append(i*10)
        values.append(i)
    print(values)

    pos=values.index(4)
    print("4 at : "+str(pos))

    values.insert(3,"cat")
    print(values)

    values.insert(1000,"dog")

    for i in range(5):
        values.append(10)
    print(values)
    numOccur= values.count(2)
    print("2 appears: " + str(numOccur) + " times.")

    pos=values.index(10)
    print("10 at : " +str(pos))

    print()
    #this removes only one occurance of a num and the first postion 
    values.remove(10)
    print(values)

##    for i in range(values.count(10)):
##        values.remove(10)
##        print(values)

    while 10 in values:
        print()
        values.remove(10)
        print(values)
    print()
    value=values.pop(2)#removes at postion 2
    print(values)
    print(value)
    #gets rid of item in list and tells the position that it is in
    for i in range(4):
        print()
        value=values.pop(2)#removes at postion 2
        
        print("removed: " +str(value))
        print(values)

        print()

    try:
        pos=eval(input("enter position to remove: "))
        value=values.pop(pos)
        print("removed: " +str(value))
        print(values)
    except IndexError:
        print("not a valid position")
    except:
        print("must enter num")


        

##    values.sort()
##    print(values)
##
##    print()
##    names=["zoo","Zebra","zion","Yodel","yak","ant","Apple"]
##    names.sort()
##    print(names)
##    #sorts basked off of askee chart. captial letters go first
##    print()
##    names.reverse()
##    print(names)
##    #sorts names by flipping the list backwards
##
##    print()
##    #method called index
##    pos= values.index(10)
##    print("10 at: " +str(pos))
##    print(values)
##    #if something is not in the list it will give an error with index
##    print()
##    try:
##    #method called index
##        pos= values.index(1000)
##    except ValueError:
##        pos=-1
##    print("1000 at: " +str(pos))
##    print(values)
##
##    ##try and error box example
##    print()
##    for i in [10,20,90,1000,7,-20,8]:
##        try:
##            pos=values.index(i)
##        except ValueError:
##            pos=-1
##        print(str(i) + " at: " + str(pos))
##    print()
##    try:
##        num = eval(input("enter a num: "))
##        print("you entered: "+str(num))
##    except NameError:
##        print("you must enter a number")
##
##    print()

    ##while they havent entered a number
        #try:
        ## get num
        #   print(statement)
        #except errorname:
        #       error message
        ##enterANum=false
        ##while not entered a num:
##    enteredANum= False
##    while not enteredANum:
##        try:
##            num = eval(input("enter a num: "))
##            enteredANum=True
##            print("you entered: "+str(num))
##        except NameError:
##            print("you must enter a number")

    
    
main()
