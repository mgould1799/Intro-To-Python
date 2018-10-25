from graphics import*

def random():
    width=400
    height=400
    win=GraphWin("random",width, height)
    win.setBackground("black")

    
    points=[Point(20,30),Point(50,60),Point(90,10)]
    shape=Polygon(points)
    shape.draw(win)
    shape.setFill("green")

    points2=shape.getPoints()
    print(points2)

    point1=points2[0]
    point2=points2[1]
    point3=points2[2]
    print(point1,point2,point3)

    point1X=point1.getX()

    print(point1X)

    win.getMouse()
    win.close()
