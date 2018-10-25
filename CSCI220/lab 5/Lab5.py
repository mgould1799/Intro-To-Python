# Lab5.py
# Name 1:
# Name 2: 

from graphics import *

def cupConverter():
    # Author: RoxAnn H. Stalvey, modified by Walter Pharr
    # Illustrates getting numeric input through graphics window
    winWidth = 300
    winHeight = 200
    win = GraphWin("Convert cups to milliliters", winWidth, winHeight)

    #Specify the message for the input box
    boxDesc = Text(Point(100, 50), "Input cups: ")
    boxDesc.draw(win)

    #Create the Entry object and set its default text to a number
    #  allowing the user to see what type of value is expected
    inp = Entry(Point(200, 50), 5)
    inp.setText("0")
    inp.draw(win)

    #Create a Text object for outputting the result
    output = Text(Point(150, 150), "")
    output.draw(win)

    #This button isn't necessary, but it makes a nice point for the user
    #  to click.  If you click anywhere in the window, the code reacts
    #  the same way.
    btPtX = winWidth/2
    btPtY = winHeight/2
    button = Text(Point(btPtX, btPtY), "Click")
    button.draw(win)
    border = Rectangle(Point(btPtX-35, btPtY-20), Point(btPtX+35, btPtY+20))
    border.draw(win)

    # Wait for a mouse click
    win.getMouse()

    # Discover intput and convert it to a number
    # If numeric input wasn't needed, simply omit the eval()
    cups = eval(inp.getText())

    #Calculate milliliter equivalent here

    # Display output and change button
    output.setText("value entered = " + str(cups))
    button.setText("Quit")
    
    # Wait for another click to exit
    win.getMouse()
    win.close()


def target():
    winWidth = 500
    winHeight = 500
    win = GraphWin("Archery Target", winWidth, winHeight)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()



def triangle():
    winWidth = 500
    winHeight = 500
    win = GraphWin("Draw a Triangle", winWidth, winHeight)

    # Add code here to accept the mouse clicks, draw the triangle.
    # and display its area in the graphics window.

    # Wait for another click to exit
    win.getMouse()
    win.close()

def colorShape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    #create window
    winWidth = 400
    winHeight = 400
    win = GraphWin("Color Shape", winWidth, winHeight)
    win.setBackground("white")

    #create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(winWidth/2, winHeight-20), msg)
    inst.draw(win)

    #create circle in window's center
    shape = Circle(Point(winWidth/2, winHeight/2 - 30), 50)
    shape.draw(win)

    #redTexPt is 50 pixels to the left and forty pixels down from center
    redTextPt = Point(winWidth/2 - 50, winHeight/2 + 40)
    redText = Text(redTextPt, "Red: ")
    redText.setTextColor("red")

    #greenTextPt is 30 pixels down from red
    greenTextPt = redTextPt.clone()
    greenTextPt.move(0,30)
    greenText = Text(greenTextPt, "Green: ")
    greenText.setTextColor("green")

    #blueTextPt is 60 pixels down from red
    blueTextPt = redTextPt.clone()
    blueTextPt.move(0,60)
    blueText = Text(blueTextPt, "Blue: ")
    blueText.setTextColor("blue")

    #display rgb text
    redText.draw(win)
    greenText.draw(win)
    blueText.draw(win)

    
    
def main():
    cupConverter()
    target()
    triangle()
    colorShape()







