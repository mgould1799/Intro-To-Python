
## lab2.py
## Purpose: Solves problems assigned in Lab 2
## Name: <your name here> 
import math
def helloWorld():
    print("Hello, world!")

def sumOfThrees():
    print("This function sums multiples of three.")

#Type each function here then call the function from main() below.
#Once the function is working correctly, you can put a comment symbol
#in front of the call in main() so that you don't have to see it run over
#and over.  An example helloWorld function is above with a commented out
#call to the working function below.

def   sumOfThrees():
     print("This program calculates the multiples of three for a given number")
     givenNumber = eval(input("Give a number: "))
     total = 0
     for i in range(givenNumber//3):
         total = total + ((i +1) * 3)
     print("The sums of three are: ", total)
        
        
## write a function to find the mulitplication for the number for 1-12
def multiplicationTable():
    print("This program will help you find the multiplation values for numbers 1-12")
    multipleNumber = eval(input("Enter a number 1-12 "))
    total = 0
    for i in range (multipleNumber):
        total = i +1
        print(total, end = " ")
    print()
    for i in range (multipleNumber):
        total2 = (i+1) * 2
        print(total2, end = " ")
    print()
    for i in range (multipleNumber):
        total3 = (i+1) *3
        print(total3, end = " ")
    print()
    for i in range (multipleNumber):
        total4=(i+1)*4
        print(total4, end=" ")
    print()
    for i in range (multipleNumber):
        total5=(i+1)*5
        print(total5, end = " ")
    print()
    for i in range (multipleNumber):
        total6=(i+1)*6
        print(total6, end=" ")
    print()
    for i in range(multipleNumber):
        total7=(i+1)*7
        print(total7, end = " ")
    print()
    for i in range(multipleNumber):
        total8=(i+1)*8
        print(total8, end =" ")
    print()
    for i in range(multipleNumber):
        total9=(i+1)*9
        print(total9, end = " ")
    print()
    for i in range (multipleNumber):
        total10=(i+1)*10
        print(total10, end =" ")
    print()
    for i in range (multipleNumber):
        total11=(i+1)*11
        print(total11, end = " ")
    print()
    for i in range(multipleNumber):
        total12= (i+1)*12
        print(total12, end =" ")
    print()

def sumSquares():
    print("This function will help you find the sums between two intergers.")
    lowerbound = eval(input("Enter the lower bound number: "))
    upperbound = eval(input("Enter the upper bound number: "))
    total=0

    for i in range (lowerbound, upperbound+1):
        total=total+i**2
    print("Total= ", total)
        
    


##this function will calculate the area of a triangle
def triangleArea():
    print("This function will help you find the area of a triangel")
    sideA= eval(input("Enter the length of side A "))
    sideB = eval(input("Enter the length of side B "))
    sideC= eval(input("Enter the length of side C "))
    s = (sideA+sideB+sideC)/2
    area = math.sqrt(s*(s-sideA)*(s-sideB)*(s-sideC))
    print("Area= ", area )

def power():
    print("This function will help you figure out the power for the base")
    base= eval(input("Enter the base: "))
    power= eval(input("Enter the power: "))
    



