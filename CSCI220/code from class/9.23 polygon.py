from graphics import *

## creates a polygon
## list of points = points=[point( ), point( )]
## witch = Polygon(points)
## accumulation and know pattern and loop and get list bigger
##nums = [] is a list
## for i ranget(4)
##      val=eval(input("num? "))
##      nums.append(val)?
## points[]= empty list
## for i in range(10):
##      clickPt=win.getMouse()
##      points.append(clickPt)
##      witch=Polygon(points)
##      witch.draw(win)


def polygon():
    Width=400
    Height=500
    win=GraphWin("Points",Width, Height)

    points=[]
    for i in range(5):
        clickPt=win.getMouse()
        clickPt.draw(win)
        points.append(clickPt)
        print("Point "+"(" + str(clickPt.getX())+"," + str(clickPt.getY())+")")

    shape=Polygon(points)
    shape.draw(win)

    win.getMouse()
    win.close()

def face():

    win=GraphWIn("face",200,200)
    winWidth=win.getWidth()
    winHeight=win.getHeight()

##alias= refers another way to refer to something in memory
##leftEye=Circle(Point(70,70),15)
##rightEye=leftEye : wrong
##whatever happens to alias happens to orginal 
##rightEye=leftEye.clone(): correct
#clone creates a replica but new memory thingie so you dont change for ex left eye
#clones are not drawn you have to draw them
#rightEye.move(60,0)
##leftEye.draw(win)
