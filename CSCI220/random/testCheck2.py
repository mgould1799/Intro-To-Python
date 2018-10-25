import math
from graphics import *
##practice problem 7 
def joinFirst(stringList):
    line=stringList
    value = ""
    for letters in line:
        
        firstLetter= letters[0]
        value+= firstLetter
    print(value)
        
def main():

    list1=["hello", "there","friend"]
    joinFirst(list1)
    print(joinFirst)

##practice problem 8

def userName():
    name= input("Enter your first, middle, and last name: ")
    nameList=name.split()
    lastName= nameList[2]
    middle = nameList[1]
    first = nameList[0]

    firstPart= lastName[:5]
    secondPart=first[:3]
    thirdPart=len(middle)

    userName= firstPart+ secondPart+ str(thirdPart)
    userName=userName.lower()

    print(userName)

## practice problem 9 ** not completely right but it will get most points?
def gradeAverage():
    infile=open("data.txt","r")
    outfile=open("average.txt","w")

    for grades in infile.readlines():
        splitList=grades.split()
        firstName=splitList[0]
        lastName=[1]
        entryName= splitList[0]+splitList[1]
        total=0
        for i in range(2,len(splitList)):
            total+=i
            print(total)
            avg=total/len(splitList)
        print(entryName, avg,file=outfile)

## practice problem 10
def distance(pt1,pt2):
    pt1X=pt1.getX()
    pt1Y=pt1.getY()
    pt2X=pt2.getX()
    pt2Y=pt2.getY()

    dx=pt2X-pt1X
    dy=pt2Y-pt1Y

    distance1=math.sqrt((dx**2)+(dy**2))
    print(distance1)
    
def main():
    win= GraphWin("random", 500,500)
    pt1=Point(3,30)
    pt2=Point(100,200)
    pt1.draw(win)
    pt2.draw(win)

    distance(pt1,pt2)
    print(distance)

##practice problem 5
def reverse(text):
    textFirstLetter=text[0]
    textRestLetter=text[1:]
    reverse=textRestLetter+textFirstLetter
    print(reverse)

def main2():
    text="hello"
    reverse(text)
    print(reverse)

def emailAdress(name):
    name2=name.split()
    first=name2[0]
    middle=name2[1]
    last=name2[2]
    part1=last[:9]
    part2=first[0]
    part3=middle[0]
    email=part1+part2+part3
    email=email.lower()
    finalEmail=email+"@g.cofc.edu"
    print("your email is: {0}".format(finalEmail))
def main3():
    name="meagan ann gould"
    emailAdress(name)
    print(emailAdress)

def calculateValues1(nums):
    for i in range(len(nums)):
        nums[i]=nums[i]+10
def calculateValues2(nums):
    values=[]
    for num in nums:
        values.append(num*2)
    print(values)
def main4():
    numbers=[7,3,5]
    print(numbers)

    calculateValues1(numbers)
    print(numbers)

    totals=calculateValues2(numbers)
    print(numbers)
    print(totals)
def avgerageAge():
    infile=("data2.txt","r")
    #fileSplit=infile.split()
    line=infile
    total=0
    for line in infile:
        fileSplit=line.split()
        grade=fileSplit[1]
        total+=grade
    avgAge=total/len(fileSplit)
    print(avgAge)

def calc1(value):
    total=0
    for i in range(0,10,value):
        total+=i
    print(total)
def calc2(values):
    total=0
    for val in values:
        val=val+1
        total+=val
    print(total)
def calc3(values):
    total=0
    for i in range(len(values)):
        values[i]=values[i]+1
        total+=values[i]
    values.append(total)

def main5():
    ans=calc1(3)
    print(ans)
    nums=[5,10,2,4]
    ans=calc2(nums)
    print(ans)
    print(nums)
    calc3(nums)
    print(nums)
