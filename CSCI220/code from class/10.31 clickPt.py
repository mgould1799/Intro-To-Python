from graphics import *

#input:rect and pt
#output: if it within a box
def didClick(rect,pt):
    rectP1=rect.getP1()
    rP1X=rectP1.getX()
    rP1Y=rectP1.getY()
    
    rectP2=rect.getP2()
    rP2X=rectP2.getX()
    rP2Y=rectP2.getY()

    ptX=pt.getX()
    ptY=pt.getY()

    if ptX>= rP1X and ptX<= rP2X:
        if ptY>= rP1Y and ptY<= rP2Y:
            rtnVal= True
        else:
            rtnVal= False
    else:
        rtnVal= False
    return rtnVal

def main():
    click=[]
    click.append(Point(50,100))
    click.append(Point(75,100))
    click.append(Point(50,125))
    click.append(Point(75,125))
    click.append(Point(30,80))

    button=Rectangle(Point(25,75),Point(60,115))
    for i in range(len(click)):
        print(didClick(button,click[i]))

main()
