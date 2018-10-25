#Name: Meagan Gould
# Purpose: create a random bumber care sequence within a graphics window
#input: parameters
#output: two random balls bounce across the screen across the monitor
#Certification of Authenticty: I certify that this is my own work.
##      I did talk to Keirm and Eduardo about this. 
from graphics import *
import random
import time
import math

##creates random move amount
def getRandom(moveAmount):
    moveAmountRun=random.randint((-1)*moveAmount,moveAmount)
    return moveAmountRun
        
## if the two bumper cars collide
def didCollide(ball,ball2):

    center1= ball.getCenter()
    center2=ball2.getCenter()
    x1=center1.getX()
    y1=center1.getY()
    x2=center2.getX()
    y2=center2.getY()

    distance= math.sqrt(((x1-x2)**2) + ((y1-y2)**2))
    radius1=ball.getRadius()
    radius2=ball2.getRadius()
    radiusTotal=radius1+radius2
    return distance <= radiusTotal
        
## if balls do hit verticle wall
def hitVertical(ball,win):
    cPt= ball.getCenter()
    centerX=cPt.getX()
    
    radius=ball.getRadius()
    width=win.getWidth()
    
    return ((centerX + radius) > width or (centerX - radius) < 0)
    
## if hits horizontal wall
def hitHorizontal(ball,win):
    cPt=ball.getCenter()
    cY=cPt.getY()
    
    height =win.getHeight()
    radius=ball.getRadius()
    
    return ((cY + radius) > height or (cY - radius) < 0)

##creates a random color
def randomColor():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return color_rgb(red, green, blue)

def main():
    ##creates window and circles
    win=GraphWin("bumper", 600,600)
    ciclePt1=Point(30,50)
    circ1=Circle(ciclePt1,20)
    circlePt2=(Point(100,400))
    circ2=Circle(circlePt2,20)
    circ1.draw(win)
    circ2.draw(win)

    
    ##variable set ups
    timeToRun=400
    moveAmount=5

    #circle to random color
    circ1.setFill(randomColor())
    circ2.setFill(randomColor())

    
    #starts circles to move at a random position
    X=getRandom(moveAmount)
    Y=getRandom(moveAmount)
    X2=getRandom(moveAmount)
    Y2=getRandom(moveAmount)

    
    ##run sequence 
    for i in range(timeToRun):
        
        if( didCollide(circ1, circ2) == True):
            X = X * (-1)
            Y = Y * (-1)
            circ1.setFill(randomColor())
            X2 = X2 * (-1)
            Y2 = Y2 * (-1)
            circ2.setFill(randomColor())
            
        if ( hitHorizontal(circ1, win) == True):
            X = X * (-1)
            Y = Y * (-1)
            circ1.setFill(randomColor())
        if ( hitHorizontal(circ2, win) == True):
            X2 = X2 * (-1)
            Y2 = Y2 * (-1)
            circ2.setFill(randomColor())
        if ( hitVertical(circ1, win) == True):
            X = X * (-1)
            Y = Y * (-1)
            circ1.setFill(randomColor())
        if ( hitVertical(circ2, win) == True):
            X2 = X2 * (-1)
            Y2 = Y2 * (-1)
            circ2.setFill(randomColor())

        circ1.move(X,Y)
        circ2.move(X2,Y2)
        time.sleep(.03)
        
            
        
        
main()
