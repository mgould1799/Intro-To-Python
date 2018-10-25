from graphics import *

##define loop- loops a certain num of times
##      (for) ex)for i in range(len(list))
# indefinate loop- loop that excutes as long as a condition is true
##      (while)
## min can run is 0 and max is infinte = (0, infinity sign)

## word="cat"
## while != "bannas":
##      tapPencil()
##      word= input("what is word? ")
## print("done")
## infinte loop goes on forever


## deMorgan's law-create new ways to say something
##not num > 100 = num <= 100

##num      not num>100           num<= 100
##99        not false->true       true
##100      not false-> true       true
##101      not true-> false       false

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

    #test if pt's x between rect x val
    #   and pt's y between rect y 
    return ptX >= rP1X and ptX <= rP2X and ptY >= rP1Y and ptY <= rP2Y

##    if ptX>= rP1X and ptX<= rP2X:
##        if ptY>= rP1Y and ptY<= rP2Y:
##            rtnVal= True
##        else:
##            rtnVal= False
##    else:
##        rtnVal= False
##    return rtnVal
##if assume false then prove true do not have to have an else statment


## indefinte loops
##continue is the not of the stop

##def getNum():
##    num = eval(input("enter a num: "))
##    while not >100: #not num > 100
##        print("num be greater than 100.")
##        num=eval(input("enter a num: "))
##    return num
        
        
def main():

    print("didClick test")
    click=[]
    click.append(Point(50,100))
    click.append(Point(75,100))
    click.append(Point(50,125))
    click.append(Point(75,125))
    click.append(Point(30,80))

    button=Rectangle(Point(25,75),Point(60,115))
    for i in range(len(click)):
        print(didClick(button,click[i]))

##    print()
##
##    print("getNum test")
##    value=getNum()
##    print("uesr entered: " + str(value))

main()
