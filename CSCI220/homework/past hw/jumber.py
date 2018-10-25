"""
Work all the T/F, Multiple Choice and Discussion for Chapter 7

T/F
1. t
2. f
3. t
4. f
5. f
6. t
7. f
8. f
9. t
10.f
Multiple Choice
1. c
2. c
3. b
4. c
5. b
6. c
7. a
8. c
9. a
10. c

Discussion
1.
a. If the suite of an if clause consists only of a single line
b. two way decisions is gives us True or false if or else
c. it is look like multiiple choice if elif or else

2.

a. trees,larch, done
b. trees,chestnut,done
c. Spam Please!,done
d. Cheese Shoppe,Cheddar,done
e. Its a late Parrot, done
f. Cheese Shoppe,Cheddar,done

3.Try / except is different form if / else because it deals directly with errors encountered in the program.
  you use Try/ except to catch errors in a program.

Name: kerim ozturk
Authenticity 

"""
from graphics import *
from time import sleep
def main():
    win = GraphWin("Jumping Jack",300,400)
    start = Button(win,Point(50,350), 80,80,'START','yellow')
    stop = Button(win,Point(150,350), 80,80,'STOP','mistyrose')
    end = Button(win,Point(250,350), 80,80,'QUIT','thistle')

       #position Zero
    p0 = Point(150,120) #c
    p1 = Point(200,200) #a
    p2 = Point(100,200) #a
    p3 = Point(150,220) #c
    p4 = Point(130,290) #l
    p5 = Point(170,290) #L

    #position One

    p6 = Point(230,120) #a
    p7 = Point(80,120) #a
    p8 = Point(230,290) #l
    p9 = Point(80,290) #L

    #position two

    p10 = Point(210,70) #arm
    p11 = Point(90,70) #arm

    
  
    positionZero = [Line(p0,p1),Line(p0,p2),Line(p3,p4),Line(p3,p5)]
    
    positionOne = [Line(p0,p6),Line(p0,p7),Line(p3,p8),Line(p3,p9)]
    
    positionTwo = [Line(p0,p10),Line(p0,p11),Line(p3,p4),Line(p3,p5)]

 
    cir = Circle(Point(150,50),45)
    cir.setFill('red')
    cir.draw(win)
    Line(Point(150,94),Point(150,220)).draw(win)

    allPositions = [positionZero,positionOne, positionTwo,positionOne]


    
    state = [0]

    for obj in allPositions [state[0]]:
        obj.draw(win)
        
    #Loop in case start wasn't clicked and for after a stop
    for i in range(100):
        #wait for a mouse click and see if start was clicked
        p = win.getMouse()
        if start.clicked(p):
            #Action loop, moving while this loop is active
            for i in range(10000):
                #Make one move and then check for mouse clicks
                jump_once(allPositions,state,win)
                sleep(0.1)
                p = win.checkMouse()
                #if stop clicked, get out of the action loop
                if stop.clicked(p):
                    break
                #If end clicked, get out of the action loop
                if  end.clicked(p):
                    break
        #If end terminated the action loop, terminate the outer loop
        if end.clicked(p):
            break
    #Close the window with no errors
    win.close()

def jump_once(allPos,state,win):
    #sample code you will have to replace with a moving stick figure
    #this function returns nothing but does update the state list with new count

    for obj in allPos [state[0]]:
        
        obj.undraw()
    state[0] = (state[0] + 1) % 4
    
    for obj in allPos [state[0]]:
        
        obj.draw(win)
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
