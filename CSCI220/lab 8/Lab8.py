# CSCI 220L - Lab 8 Solutions
#
# Name 1: Meagan G.
#
# Name 2: Carter
#

def formatPractice():
    print("It's raining {1} and {0}".format("dogs","cats"))
    print("{0:1.2f} {1:0.3f}".format(float(2.3),float(.4567)))
    print("{0:02}" ":" "{1:05.2f}".format(int(3), 7.4567))
    print("{0} {1}: {2:04.2f}".format("Steph", "Curry", float(43.75432)))

def encode():
    codeMessage=input("enter a word to be encoded: ")
    message=[]
    text=""
    key = eval(input("enter a key: "))
    for characters in codeMessage.lower():
        message+=characters
        
    for ch in message:
        text+= chr(ord(ch)+int(key))
            
            
        
    
    print(text)

def encodeBetter():
    message = input("Enter your message: ")
    key = eval(input("enter a key: "))
    characters = []
    newMessage = ""
    for character in message.lower():
        characters += character
    for letter in characters:
        newMessage+= chr(((((ord(letter)- ord("a"))+int(key)) % 26) +ord("a")))
    print(newMessage)

def addTen(nums):
    for i in range(len(nums)):
        nums[i]=nums[i]+10

def squareEach(strList):
    for i in range(len(strList)):
        strList[i]= strList[i]**2

def sumList(nums):
    total=0
    for i in range(len(nums)):
        total+=nums[i]
    return total

def toNumber(strList):
    for i in range(len(strList)):
         strList[i] = float(strList[i])



def sumOfSquares():
    list1 = [2,3,4,5]
    print(list1)
    squareEach(list1)
    print(list1)

    list2=[1,3]
    sum2=sumList(list2)
    print(list2)
    print(sum2)

    list3 = ["3","5.7","2"]
    print(list3)
    toNumber(list3)
    print(list3)
    
sumOfSquares()


        
        

##function to test code in problem 4.  Do not run
##until addTen() is written
def testTens():
    values = [5, 2, -3]
    print(values)
    addTen(values)
    print(values)
