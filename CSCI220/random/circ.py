from graphics import *

def circ():
    height = 500
    width = 500
    win= GraphWin("Click to move cirlce", height, width)


    pt=Point(200, 300)
    pt.draw(win)

    circ=Circle(pt,100)
    circ.draw(win)
    circ.setFill("grey")

    win.getMouse()
    win.close()
    
