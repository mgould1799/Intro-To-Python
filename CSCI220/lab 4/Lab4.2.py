"""
Lab 3 - Graphics
Name:
"""


## Discussion #3, Graphics chapter of Zelle text
## Moves a circle based on user clicks
## Comments added: RHS

from graphics import *
import math

def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    #Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    #number of times user can move circle
    numClicks = 5

    #create a space to instruct user
    instPt = Point(width/2, height-10)
    instructions = Text(instPt,"Click to move square")
    instructions.draw(win)

    ptA=Point(100, 50)
    ptB=Point(150,100)

    #builds a square
    shape = Rectangle(ptA,ptB)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)



    #allows the user to click multiple times to move the
    #circle
    for i in range(numClicks):
        p = win.getMouse()
        c = shape.getCenter() #center of circle
        shape2 = shape.clone()
        shape2.draw(win)

        #move amount is distance from center of circle to the
        #point where the user clicked
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape2.move(dx, dy)
        

    win.getMouse()
    win.close()

def rectangle():
    width=600
    height=600
    win=GraphWin("Lab 4",width, height)

    p = win.getMouse()
    px=p.getX()
    py=p.getY()
    p2=win.getMouse()
    p2X=p2.getX()
    p2Y=p2.getY()
   
    rect=Rectangle(p,p2)
    rect.setFill("blue")
    rect.draw(win)

    height = abs(p2X-px)
    width = abs(p2Y-py)
    area=height*width
    perimeter=2*(height+width)
    randPt=Point(400,300)
    perimeter=Text(randPt, "Perimeter= " +str(perimeter))
    randPt2= Point(500,400)
    area=Text(randPt2, "Area= "+ str(area))
    perimeter.draw(win)
    area.draw(win)

    win.getMouse()
    win.close()

def circle():
    width=400
    height=400
    win=GraphWin("Lab 4",width, height)
    centerPt=win.getMouse()
    centerPtX=centerPt.getX()
    centerPtY=centerPt.getY()
    circumPt=win.getMouse()
    circumPtX=circumPt.getX()
    circumPtY=circumPt.getY()

    radius = math.sqrt(((circumPtX-centerPtX)**2)+((circumPtY-centerPtY)**2))
    circ= Circle(centerPt, radius )
    circ.setFill("yellow")
    circ.draw(win)

    win.getMouse()
    win.close()

def pi2():
    NUM=4
    PI=math.pi
    denom=0
    numOfTimes=eval(input("Enter how many times you would like to run the loop: "))
    for i in range(numOfTimes):
        denmon= denom +(i+1)+2
        
##def main():
    ##squares()
##    rectangle()
##    circle()
##    pi2()
##    pi()

##main()
