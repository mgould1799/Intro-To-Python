# Lab6.py
# Name 1: Meagan Gould
# Name 2: Trett Hudson

def nameReverse():
 name= input("Enter your first name and last name: ")
 nameList=name.split()

 first=nameList[0]
 last=nameList[1]

 nameReverse= print(last + ", " + first)

def companyName():
    url = input("Enter URL Here:")
    urlList = url.split(".")
    companyName = urlList[1].title()
    print(companyName)

def initials():
    numStudents = eval(input("Enter how many students in class: "))
    for i in range(numStudents):
        firstName= input("Enter first Name of student # " + str(i +1) +": ")
        lastName= input("Enter %s's last name :" % firstName)
        initials= (firstName[0]+lastName[0]).upper()
        print("%s's initials are: "%firstName, initials)

def names():
    names= input("Enter people's first and last names, seperated by commas: ")
    namesList = names.split(",")
    initialsString = ""
    for name in namesList:
        nameSplit = name.split()
        first = nameSplit[0]
        last = nameSplit[1]
        initials = (((first[0] + last[0]).upper()) + " ")
        initialsString += initials
    print("The initials are: ", initialsString)

def thirds():
    sentNum=eval(input("Enter how many sentences you are inputing: "))
    for i in range(sentNum):
        sent=input("Enter Sentence # " + str(i+1))
        for j in range(2,len(sent),3):
            print(sent[j], end="")

def wordCount():
    sentNum = eval(input("Enter the number of sentences to be input:"))
    for i in range(sentNum):
        sent = input("Enter the sentence Here: ")
        sentList = sent.split()
        numWords = len(sentList)
        print(numWords)
def wordAverage():
    total = 0
    sentNum=eval(input("Enter the number of sent to be inputed: "))
    for i in range(sentNum):
        sent=input("Enter sent #" + str(i+1) +": ")
        sentList=sent.split()
        numChs = (len(sent)) - (sent.count(" "))
        numWords=len(sentList)
        print("Average word length: ", str(numChs / numWords))

def pigLatin():
    sent = input("Enter Sentence to be translated here: ")
    sentList = sent.split()
    numWords = len(sentList)
    for words in sentList:
        let1 = words[0]
        otherLets = words[1:]
        ay = "ay"
        newWord = (otherLets + let1 + ay).lower()
        print(newWord, end=" ")
        
##def main():
##    nameReverse()
##    #add other function calls here
##
##main()
    
