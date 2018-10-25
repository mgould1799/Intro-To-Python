#Name: Meagan Gould
#Input: parameters into smaller functions by clicking on screen to get coordinates
##              for a triangle.
##Output: a triangle, distance, area, and perimeter all on too a screen created
##              by the graphics package
##Purpose: to give the distance between two points, area, and perimeter for a triangle
##Certification of Authenticity: I certify that this is my own work. 
# triangle.py
# Author: Zelle (pp. 103-04)
# Modified by Pharr to eliminate coordinates


from graphics import *
import math

##input: points
#output: creates a triangle
def makeTriangle(pt1,pt2,pt3):
    points=[pt1,pt2,pt3]
    triangle=Polygon(points)
    return triangle

#input: two points from the triangle 
#output: returns a distance formula 
def distance(pt1,pt2):

    #gets x and y for 2 points
    p1X=pt1.getX()
    p1Y=pt1.getY()
    p2X=pt2.getX()
    p2Y=pt2.getY()

    #finds distance
    distance = math.sqrt(((p2X-p1X)**2)+((p2Y-p2X)**2))
    return distance

#input:triangle
#output:returns a triangle's perimeter
def perimeter(tri):
    pointList = tri.getPoints()
    point1=pointList[0]
    point2=pointList[1]
    point3=pointList[2]

    distance1=distance(point1,point2)
    distance2=distance(point2,point2)
    distance3=distance(point3,point1)

    perimeter= distance1+distance2+distance3
    return perimeter

#input: a triangle/ parameter
#output: returns the area of a triangle
def area(tri):

    #gets points
    pointList = tri.getPoints()
    point1=pointList[0]
    point2=pointList[1]
    point3=pointList[2]
    
    #gets distance
    distance1=distance(point1,point2)
    distance2=distance(point2,point2)
    distance3=distance(point3,point1)
    
    #finds area
    semiPerimeter= (distance1+distance2+distance3)/2
    area=(semiPerimeter*(semiPerimeter-distance1)*(semiPerimeter-distance2)*(semiPerimeter-distance3))**.5
    return area


def main():
    winWidth = 400
    winHeight = 400
    
    win = GraphWin("Draw a Triangle", winWidth, winHeight)
    message = Text(Point(winWidth/2, winHeight-10), "Click on three points")
    message.draw(win)

    # Get and draw three vertices of a triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # Use Polygon object to draw the triangle
    triangle = makeTriangle(p1,p2,p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)
    
    
    #finds perimeter
    perimeter1= perimeter(triangle)

    #finds area
    area1= area(triangle)

    #outputs area and perimeter to the win box
    output1= Text(Point(200,350), "")
    output2=Text(Point(200,370),"")
    output1.draw(win)
    output2.draw(win)
    output1.setText("The perimeter is: {0:0.1f}".format(perimeter1))
    output2.setText("The area is: {0:0.1f}".format(area1))
    
    

    # Wait for another click to exit
    message.setText("Click anywhere to quit")
    win.getMouse()
    win.close()

main()
