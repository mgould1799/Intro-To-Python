## Meagan Gould
## lab3.py

from graphics import *

#Calculate the average of a group of numbers per assignment instructions
def average():
    print("Finds average")

#Example graphics program
def makeCircle():
    #creates the window
    winWidth = 300
    winHeight = 400
    win = GraphWin("Click a point", winWidth, winHeight)
    win.setBackground("yellow")

    #creates a Point object that is centered in the window
    center = Point(winWidth//2, winHeight//2)

    #draws a blue circle around center point
    ball = Circle(center, 20)
    ball.setFill("blue")
    ball.draw(win)
        
    #creates and displays instructions
    instructPoint = Point(winWidth//2, winHeight - 10)
    instructions = Text(instructPoint, "Click window to close.")
    instructions.draw(win)

    #Allows the user to click the window and then closes window
    clickPt = win.getMouse()
    win.close()

def buildHouse():
    winWidth = 400
    winHeight = 500
    win = GraphWin("Click a point", winWidth, winHeight)
    win.setBackground("blue")
    pointA= point(0,400)
    pointB= point(0, 300)
    
def main():
    average()
    #fibonacci()
    #newton()
    #sequence()
    #pi()

def average():
    print("This program will you find the average of grades that you are inputting")
    total = 0
    numGrades = eval(input("Enter how many grades you are averaging: "))
    for i in range(numGrades): 
        gradeTotal = eval(input("Enter grade on HW #" + str(i +1)+": "))
        total = total+gradeTotal
    totalGrade = (total) / numGrades
    print("The average is: ", totalGrade)

def fibonacci():
    print("This program will help you figure out a fibonacci sequence")
    fibNum = eval(input("Enter a number to compute the fibonacci sequence: "))
    start1= 0
    start2= 1
    temp = 0
    for i in range(fibNum):
        temp = start1
        start1= start2
        start2=temp + start2
        print(temp)
    print()
    
def newton():
    print("This program will help you approixmate the square root of a function using newtown's square root formula")
    sqRoot = eval(input("Enter the number you wish to approximate the squarte root of: "))
    approxTimes=eval(input("Enter the number of times you wish to approximate the square root by: "))
    approx = sqRoot/2
    for i in range(approxTimes):
        approx = (approx +(sqRoot/approx))/2
    print(approx)


    
