from graphics import *

def circRadius():
    win=GraphWin("bleh",500,500)
    cir=Circle(Point(200,80),60)
    cir.setFill("blue")
    cir.draw(win)
    radius=cir.getRadius()
    print("radius: ", radius)
    height=win.getHeight()
    print("height: ",height)

    
