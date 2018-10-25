from graphics import *
import time

def main():
    win=GraphWin("my first window", 500, 300)
    win.setBackground("blue")

    ptA=Point(50,100)
    cir =Circle(ptA, 20)
    cir.setFill("yellow")
    cir.draw(win)
    for i in range(15):
        time.sleep(.5)
        cir.move(10,-15)
        time.sleep(.5)
        cir.move(10,15)
