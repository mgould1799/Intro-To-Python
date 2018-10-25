'''Program to implement bumper circles'''
" kerim ozturk"
"joshua yates"

from graphics import *
from time import sleep
from random import randint
RADIUS = 10

def main():
    '''This program creates two cicrles, one red at (150,250) and one blue
    at (350,250) that move in a set random direction. Code to set the random
    direction, x direction (-3 to +3) and y direction (-3 to 3), is provided.
    Make the radius of each circle 50, a CONSTANT that is easy to change.
    When a circle hits a vertical wall, the x direction reverses. When a circle
    hits a horizontal wall, the y direction reverses. When the circles collide,
    both circles reverse both x and y direction. Build a box for travel that
    is 500 by 500 and make the graphics window 500 by 600 with room for buttons
    in the bottom 100 pels. Begin with a loop of 100 movements'''

    # create the board and the circles
    win = GraphWin('board',500,600)
    box = Rectangle(Point(0,0),Point(500,500))
    circ1 = Circle(Point(150,250),RADIUS)
    circ1.setFill('red')
    circ1.draw(win)
    circ2 = Circle(Point(350,250),RADIUS)
    circ2.setFill('blue')
    circ2.draw(win)
    box.draw(win)
    

    #create the velocity list: velocity = [x_red, y_red, x_blue, y_blue]    
    velocity = [randint(0,6) - 3,randint(0,6) - 3,
               randint(0,6) - 3,randint(0,6) - 3]
    
 
    print (velocity) # to the shell
    
    #Motion loop
    while True:
        move_circles(circ1,circ2,velocity)
        if hit_vert_wall(circ1):
            velocity[1] = velocity[1]*-1
        if hit_vert_wall(circ2):
            velocity[3] = velocity[3]*-1
        if hit_horiz_wall(circ1):
            velocity[0] = velocity[0]*-1
        if hit_horiz_wall(circ2):
            velocity[2] = velocity[2]*-1
        if collided(circ1,circ2):
            velocity[0] = velocity[0]*-1
            velocity[1] = velocity[0]*-1
            velocity[2] = velocity[0]*-1
            velocity[3] = velocity[0]*-1
def move_circles(circle_one,circle_two,vel_xy):
    '''Moves the circles as specified in velocity. Move both circles
    each time this function executes, the red circle moves a distance of
    x_red in the x direction and y_red in the y direction. The blue circle
    moves x_blue and y_blue.'''

    
    circle_one.move(vel_xy[0],vel_xy[1])
    circle_two.move(vel_xy[2],vel_xy[3])
        
        
            
    


def hit_vert_wall(circle):
    '''Check to see if the circle has hit a vertical
    wall and return True if it has. If not, return False.
    Use getCenter method to know the position'''
    centerPt = circle.getCenter()
    centerY = centerPt.getY()
    return centerY >=(500-RADIUS) or centerY<=(RADIUS)
def hit_horiz_wall(circle):
    '''Check to see if the circle has hit a horizontal
    wall and return True if it has. If not, return False.
    Use getCenter method to know the position'''
    centerPt = circle.getCenter()
    centerX = centerPt.getX()
    return centerX >=(500-RADIUS) or centerX<=(RADIUS)
   
def collided(circle1, circle2):
    '''Check to see if the circles have collided, i.e. overlapping and
    return True if the circles have collided (touching or overlapping)
    and False if they are not overlapping'''
    
    c1 = circle1.getCenter()
    c2 = circle2.getCenter()
    x1 = c1.getX()
    x2 = c2.getX()
    y1 = c1.getY()
    y2 = c2.getY()
    distance = (((x1-x2)**2) + ((y1-y2)**2))**(1/2)
    return distance <=(2*RADIUS)
        

class Button:
    """A button is a labeled rectangle in a window. The clicked(p)
    method returns true if the button is active and p is inside it.
    The button is drawn when it is created"""

    def __init__(self, win, center, width, height, label,color):
        """
        Creates and draws a rectangular button, eg:
        qb = Button(win,Point(50,50),75,75,'Quit','tan')
        """ 
        self.p1 = Point(center.getX() - width/2, center.getY() - height/2)
        self.p2 = Point(center.getX() + width/2, center.getY() + height/2)
        self.rect = Rectangle(self.p1,self.p2)
        self.color = color
        self.rect.setFill(color)
        self.rect.setWidth(2)
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        
    def setLabel(self,label):
        self.label.setText(label)

    def setFill(self,color):
        self.rect.setFill(color)
        self.color = color
        
    def undraw(self):
        self.rect.undraw()
        self.label.undraw()

    def move(self,dx,dy):
        self.rect.move(dx,dy)
        self.label.move(dx,dy)

    def clicked(self, p):
        "Returns True if p is not None and p is inside the button"
        if p == None: return False
        return (self.p1.getX() <= p.getX() <= self.p2.getX() and
                self.p1.getY() <= p.getY() <= self.p2.getY())

   
main()       
