##Name:Meagan Gould
##this program creates a follow creeding card that flickers and says happy fall
##input:points created by the user
##output: pumpkin, ghost, mouth, eyes, happy fall, and boo all onto the screen
##Certification of Authenticity:
##I certify that this homework is entirely my own work

from graphics import *
import time

def fallGreeting():

    ## creating of window
    height = 600
    width = 800
    win= GraphWin("Fall Greeting Card", width, height)
    win.setBackground("black")

    
##    ##creating of circle for pumpkin
    circPt= Point(400,350)
    circ= Circle(circPt, 150)
    circ.draw(win)
    circ.setFill("orange")
    circ.setOutline("black")
    

    ##greeting 
    ptText= Point(400,50)
    greeting= Text(ptText, "Happy Fall")
    greeting.setFill("yellow")
    greeting.setSize(36)
    greeting.draw(win)
    

    ##eye 1
    pointsEye1=[Point(350,280),Point(373,320),Point(326,320)]
    eye1=Polygon(pointsEye1)
    eye1.draw(win)
    eye1.setFill("black")

    ##eye 2
    pointsEye2_2=[Point(452,280),Point(428,320),Point(475,320)]
    eye2=Polygon(pointsEye2_2)
    eye2.draw(win)
    eye2.setFill("black")

    ##nose
    pointNose=[Point(403,348),Point(387,372),Point(422,372)]
    nose=Polygon(pointNose)
    nose.draw(win)
    nose.setFill("black")

    ##mouth
    pointMouth=[Point(334,375),Point(357,391),Point(395,397),Point(429,400),Point(464,387),Point(478,381),Point(479,408),Point(459,427),Point(435,440),Point(415,442),Point(388,438),Point(359,428),Point(344,410),Point(334,390)]
    mouth=Polygon(pointMouth)
    mouth.draw(win)
    mouth.setFill("black")

    ##mouth square
    pointMouthSq=[Point(427,397),Point(432,414),Point(453,410),Point(450,390)]
    mouthSq1=Polygon(pointMouthSq)
    mouthSq1.draw(win)
    mouthSq1.setFill("orange")
    mouthSq1.setOutline("orange")

    ##mouth square 2
    pointMouthSq2=[Point(364,436),Point(369,414),Point(392,421),Point(387,443)]
    mouthSq2=Polygon(pointMouthSq2)
    mouthSq2.draw(win)
    mouthSq2.setFill("orange")
    mouthSq2.setOutline("orange")

    ##stem/hat
    stemPt=[Point(416,200),Point(439,136),Point(539,166),Point(503,243)]
    stem=Polygon(stemPt)
    stem.draw(win)
    stem.setFill("brown")
    hatEndPt=[Point(433,184),Point(397,174), Point(396,199),Point(428,203)]
    hatEnd=Polygon(hatEndPt)
    hatEnd.draw(win)
    hatEnd.setFill("brown")
    hatEnd.setOutline("brown")
    hatEndPt2=[Point(504,244),Point(526,255),Point(538,227),Point(508,218)]
    hatEnd2=Polygon(hatEndPt2)
    hatEnd2.draw(win)
    hatEnd2.setFill("brown")
    hatEnd2.setOutline("brown")

    for i in range(10):
        time.sleep(.5)
        eye1.setFill("yellow")
        eye2.setFill("yellow")
        mouth.setFill("yellow")
        nose.setFill("yellow")
        time.sleep(.5)
        eye1.setFill("black")
        eye2.setFill("black")
        mouth.setFill("black")
        nose.setFill("black")

    ##ghost1
    ghostPt1=[Point(88,97),Point(152,96),Point(187,143),Point(210,201),Point(232,247),
              Point(189,243),Point(155,241),Point(150,276),Point(111,255),
              Point(103,297),Point(83,282),Point(66,238),Point(60,180),Point(63,123)]
    ghost1=Polygon(ghostPt1)
    ghost1.draw(win)
    ghost1.setFill("white")

    ##ghost 2
    ghostPt2=[Point(683,376),Point(727,400),Point(742,446),Point(744,494),Point(733,544),
              Point(707,521),Point(686,537),Point(656,508),Point(627,524),Point(615,476),
              Point(615,416),Point(645,386)]
    ghost2=Polygon(ghostPt2)
    ghost2.draw(win)
    ghost2.setFill("white")

    #eyes for ghost 1
    eyeGhostPt1_1=Point(133,154)
    eyeGhostPt1_2=Point(103,165)
    eyeGhost1_1=Circle(eyeGhostPt1_1,6)
    eyeGhost1_2=Circle(eyeGhostPt1_2,6)
    eyeGhost1_1.draw(win)
    eyeGhost1_1.setFill("black")
    eyeGhost1_2.draw(win)
    eyeGhost1_2.setFill("black")
    
    #ghost eye 2
    eyeGhostPt2_1=Point(699,430)
    eyeGhostPt2_2=Point(667,431)
    eyeGhost2_1=Circle(eyeGhostPt2_1,6)
    eyeGhost2_2=Circle(eyeGhostPt2_2,6)
    eyeGhost2_1.draw(win)
    eyeGhost2_1.setFill("black")
    eyeGhost2_2.draw(win)
    eyeGhost2_2.setFill("black")
    
    #boo text 1
    booTextPt1=Point(671,168)
    booText1=Text(booTextPt1,"BOO!")
    booText1.setFill("yellow")
    booText1.setSize(27)
    booText1.draw(win)

    ##boo text 2
    booTextPt2=Point(96,507)

    booText2=Text(booTextPt2,"BOO!")
    booText2.setFill("yellow")
    booText2.setSize(27)
    booText2.draw(win)
    


##    ##import image
##    myImage= Image(Point(400,300),"cat.gif")
##    myImage.draw(win)
##    win.mainloop()

##    points=[]
##    for i in range(15):
##        clickPt=win.getMouse()
##        clickPt.draw(win)
##        points.append(clickPt)
##        print("Point " +"(" + str(clickPt.getX())+","+str(clickPt.getY())+")")
        

   ##close to exit statement
    closePt=Point(400,550)
    close=Text(closePt,"Click to Close")
    close.setFill("yellow")
    close.draw(win)
    

    win.getMouse()
    win.close()
    
    
    
