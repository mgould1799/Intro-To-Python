## Lab9.py
##
## Name 1: Bobbi-Jo C.
##
## Name 2: Meagan G.
##

from graphics import *
from math import sqrt
import math

def starter():
    """
    Ask for a wrestler's weight and number of wins, determine whether
    the wrestler is a starter.
    """
    weight = float(eval(input("What is the player's weight? ")))
    numWins = int(eval(input("How many wins does the player have? ")))
    if weight >= 150 and weight < 160 or weight > 199 or numWins > 20:
        if numWins >= 5:
            print("the person should start")
        else:
            print("person should not start")
    else:
        print("person should not start")

def isValid(isbn):
    rtnVal = False
    if len(isbn) == 10:

        pos=11
        total=0
        for i in range(len(isbn)):
            pos-=1
            total+= int(isbn[i])*(pos)
            
        mod=total%11
        if mod == 0:
            rtnVal = True
        
    return rtnVal

def circleOverlap():
    """
    Draw two circles and determine whether they overlap.
    """
    #Build window
    winHeight = 400
    winWidth = 400
    win = GraphWin("Overlapping circles", winHeight, winWidth)

    #Text area for instructions for user
    instruct = Text(Point(winWidth/2, winHeight-10), "")
    instruct.draw(win)
    instruct2 = Text(Point(winWidth/2, winHeight-30), "")
    instruct2.draw(win)
    #Get center point and x/y for center
    instruct.setText("To draw a circle, click the centerpoint for the circle")
    center = win.getMouse()
    center.draw(win)
    cX = center.getX()
    cY = center.getY()

    

    #Get point on the circumference and its x/y coordinates
    instruct.setText("Click a point on the border of the circle.")
    border = win.getMouse()
    bX = border.getX()
    bY = border.getY()

   
    #Calculate radius using Euclidean distance
    radius = sqrt((cX-bX) ** 2 + (cY-bY) ** 2)
    circle = Circle(center, radius)
    circle.draw(win)


    instruct2.setText("Click the centerpoint for circle 2")
    center2 = win.getMouse()
    center2.draw(win)
    c2X = center2.getX()
    c2Y = center2.getY()

    instruct2.setText("Click a point on the border of circle 2.")
    border2 = win.getMouse()
    b2X = border2.getX()
    b2Y = border2.getY()

    radius2 = sqrt((c2X-b2X) ** 2 + ((c2Y-b2Y) ** 2))
    circle2 = Circle(center2, radius2)
    circle2.draw(win)

    distance = math.sqrt(((c2X - cX) ** 2) + ((c2Y - cY) ** 2))
    
    circleRads = radius + radius2
    
    if distance > circleRads:
        instruct2.setText("The circles do not overlap")
    else:
        instruct2.setText("The circles do overlap")
    
    # Wait for another click to exit
    instruct.setText("Click anywhere to close.")
    win.getMouse()
    win.close()

def leapYear(year):
    
    num4= year%4
    num100=year%100
    num400=year%400
    if num4==0 and num100!=0 or num400==0:
        val= True
    else:
        val= False
    return val

def main():
    ''' Add code to test all of your functions '''
    starter()
    var="91"
    valid=isValid(var)
    print(valid)

    circleOverlap()

    year=[2000,2100,1996,1995]
    for i in range(len(year)):
        learp=leapYear(year[i])
        if learp == True:
            print(str(year[i])+" is a leap year")
        else:
            print(str(year[i])+" is not a leap year")
    
main()
