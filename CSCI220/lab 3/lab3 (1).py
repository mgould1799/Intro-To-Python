## <your name>
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
    
def main():
    average()
    #fibonacci()
    #newton()
    #sequence()
    #pi()
