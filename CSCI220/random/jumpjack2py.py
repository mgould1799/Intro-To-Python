#Name: Meagan Gould
# purpose: create a program that simulates a stick figure doing jumping jacks
#   based off of which click they chose: start, stop, close
## input: a click from the user
## output: jack jumps or stops or window closes
## Certification of Authenticty: I certify that this is my own work

from graphics import *
import time
##look at notes 10.31

##input: a point and a rectangle
#output: if the the point was clicked or not
def wasClicked(pt,rect):
    if pt==None:
        returnVal= False
    else:
        rectP1=rect.getP1()
        rP1X=rectP1.getX()
        rP1Y=rectP1.getY()
    
        rectP2=rect.getP2()
        rP2X=rectP2.getX()
        rP2Y=rectP2.getY()

        ptX=pt.getX()
        ptY=pt.getY() 

        returnVal=ptX >= rP1X and ptX <= rP2X and ptY >= rP1Y and ptY <= rP2Y
    return returnVal

def main():
    ##creates window
    win=GraphWin("jumpingJack",800,800)
    win.setBackground("black")
    
    ##creates head
    headPt=Point(380,100)
    head=Circle(headPt,100)
    head.draw(win)
    head.setFill("red")

    ##creates body 
    bodyPt1=Point(380,200)
    bodyPt2=Point(380,500)
    body=Line(bodyPt1,bodyPt2)
    body.draw(win)
    body.setFill("red")

    ##creates arm 1
    #positon 1
    armPt1_1=Point(380,300)
    armPt2_1=Point(475,150)
##    arm1Pos1=Line(armPt1_1,armPt2_1)
##    arm1Pos1.draw(win)
##    arm1Pos1.setFill("red")
    #position 2
    armPt1_2=Point(380,300)
    armPt2_2=Point(475,250)
##    arm1Pos2=Line(armPt1_2,armPt2_2)
##    arm1Pos2.draw(win)
##    arm1Pos2.setFill("blue")
    #position 3
    armPt1_3=Point(380,300)
    armPt2_3=Point(475,400)
##    arm1Pos3=Line(armPt1_3,armPt2_3)
##    arm1Pos3.draw(win)
##    arm1Pos3.setFill("yellow")

    ##creates arm 2
    #position 1
    arm2Pt1_1=Point(380,300)
    arm2Pt2_1=Point(275,150)
##    arm2Pos1=Line(arm2Pt1_1,arm2Pt2_1)
##    arm2Pos1.draw(win)
##    arm2Pos1.setFill("red")
    #position 2
    arm2Pt1_2=Point(380,300)
    arm2Pt2_2=Point(275,250)
##    arm2Pos2=Line(arm2Pt1_2,arm2Pt2_2)
##    arm2Pos2.draw(win)
##    arm2Pos2.setFill("blue")
    #position 3
    arm2Pt1_3=Point(380,300)
    arm2Pt2_3=Point(275,400)
##    arm2Pos3=Line(arm2Pt1_3,arm2Pt2_3)
##    arm2Pos3.draw(win)
##    arm2Pos3.setFill("yellow")

    ##creates leg 1
    #positon 1 
    legPt1_1=Point(380,500)
    legPt2_1=Point(475,600)
##    legPos1=Line(legPt1_1,legPt2_1)
##    legPos1.draw(win)
##    legPos1.setFill("red")
    #postion 2
    legPt1_2=Point(380,500)
    legPt2_2=Point(445,600)
##    legPos2=Line(legPt1_2,legPt2_2)
##    legPos2.draw(win)
##    legPos2.setFill("blue")
        #postion 3
    legPt1_3=Point(380,500)
    legPt2_3=Point(430,600)
##    legPos3=Line(legPt1_3,legPt2_3)
##    legPos3.draw(win)
##    legPos3.setFill("yellow")

    ##creates leg 2
    leg2Pt1_1=Point(380,500)
    leg2Pt2_1=Point(275,600)
##    leg2Pos1=Line(leg2Pt1_1,leg2Pt2_1)
##    leg2Pos1.draw(win)
##    leg2Pos1.setFill("red")
        #postion 2
    leg2Pt1_2=Point(380,500)
    leg2Pt2_2=Point(310,600)
##    leg2Pos2=Line(leg2Pt1_2,leg2Pt2_2)
##    leg2Pos2.draw(win)
##    leg2Pos2.setFill("blue")
        #postion 3
    leg2Pt1_3=Point(380,500)
    leg2Pt2_3=Point(325,600)
##    leg2Pos3=Line(leg2Pt1_3,leg2Pt2_3)
##    leg2Pos3.draw(win)
##    leg2Pos3.setFill("yellow")

    ##creates start button
    startButtonPt1=Point(620,50)
    startButtonPt2=Point(790,200)
    startButton=Rectangle(startButtonPt1,startButtonPt2)
    startButton.draw(win)
    startButton.setFill("grey")
    startTextPt=Point(700,100)
    startText=Text(startTextPt,"start")
    startText.draw(win)
    startText.setFill("black")

    ##creates stop button
    stopButtonPt1=Point(620,225)
    stopButtonPt2=Point(790,375)
    stopButton=Rectangle(stopButtonPt1,stopButtonPt2)
    stopButton.draw(win)
    stopButton.setFill("grey")
    stopTextPt=Point(700,325)
    stopText=Text(stopTextPt,"stop")
    stopText.draw(win)
    stopText.setFill("black")
    
    ##creates exit button
    exitButtonPt1=Point(620,400)
    exitButtonPt2=Point(790,550)
    exitButton=Rectangle(exitButtonPt1,exitButtonPt2)
    exitButton.draw(win)
    exitButton.setFill("grey")
    exitTextPt=Point(700,500)
    exitText=Text(exitTextPt,"exit")
    exitText.draw(win)
    exitText.setFill("black")
    

    ##groups of postion of the lips
    position1=[Line(leg2Pt1_3,leg2Pt2_3),Line(legPt1_3,legPt2_3),Line(arm2Pt1_3,arm2Pt2_3),Line(armPt1_3,armPt2_3)]
    position2=[Line(leg2Pt1_2,leg2Pt2_2),Line(legPt1_2,legPt2_2),Line(arm2Pt1_2,arm2Pt2_2),Line(armPt1_2,armPt2_2)]
    position3=[Line(leg2Pt1_1,leg2Pt2_1),Line(legPt1_1,legPt2_1),Line(arm2Pt1_1,arm2Pt2_1),Line(armPt1_1,armPt2_1)]
    position=[position1,position2,position3]
    click1=True
    
    
    i=1
    while click1 !=False:
        click=win.getMouse()
        while wasClicked(click,startButton)==True:

            i=i+1
            if wasClicked(click,startButton)==True:
                position[i%4].draw(win)
                position[i-1%4].undraw()
                time.sleep(.7)

            click2=win.checkMouse()
                
                
            if wasClicked(click2,stopButton) ==True:
                click=win.checkMouse()
                
            elif wasClicked(click2,exitButton)==True:
                
                win.close()
            click2=win.checkMouse()

                    


                
            
                    
                    
        
        
        
main()
