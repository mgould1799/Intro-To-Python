## Lab1.py
## CSCI 220L
## Meagan Gould

import math

#Simple function to print statement to user
def main():
    print("Programming is fun, but it is not a spectator sport.")
    print("I look forward to learning to control this computer through programming!")
    print("Hello, world")
    print("Hello", "world")
    print("2" + "3")
    print(2+3)
    print(2 * 3)
    print("2" * 3)

 
##This function calculates the area of a rectangle
def calcRectArea():
    print("Calculates the area of a rectangle.")
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print ("Area =", area)
    

##this function calculates the volume of a cylinder
def calcCylinderVolume():
    print("This program calculates the volume of a cylinder")
    PI=math.pi
    radius=eval(input("Enter the radius "))
    height=eval(input("Enter the height "))
    volume= PI * radius ** 2 * height
    print("Area= ", volume)
    
##find the percantages of shots for a basketball player
def shootingPercentage():
    print("This program will help you find your shooting percentages in basketball")
    totalshots=eval(input("enter total shots "))
    shotsmade=eval(input("enter total shots made "))
    percentageshots= (shotsmade / totalshots)*100
    print("your percentage of shoots is: ", percentageshots)

## computes the cost to ship coffee per a pound

def coffee():
    print("This program will help you figure out how much coffee is to ship per a pound")
    pounds = eval(input("Enter how many pounds of coffee you are ordering "))
    COFFEEPERPOUND = 10.50
    SHIPPINGPERPOUND = .86
    FIXED = 1.5
    totalcost = (pounds * COFFEEPERPOUND) + ( pounds * SHIPPINGPERPOUND )  + FIXED
    print("Your total price to ship coffee is ", totalcost)

## computes kilometers to miles
def kilometersToMiles():
    print("This program will help you convert kilometers to miles")
    kilometers = eval(input("Enter how many kilometeres have you travled "))
    MILES = 1.61
    totalmiles = MILES / kilometers
    print("Your total miles is ", totalmiles)
    
    
    
