import math

#Input: name - through the parameter list
#Output: prints the banana song to the monitor
def bananaSong(name):
    nameEnd = name[1:].lower()
    print(name + ", " + name + ", " + "bo-b" + nameEnd)
    print("Bananan-fana fo-f" + nameEnd)
    print("Fee-fy-mo-m" + nameEnd)
    print(name + "!")

#Input: Two numbers as parameters
#Output: The sum of the numbers, returned to the calling point
def addTwo(num1, num2):
    total = num1 + num2
    return total

#Input: parameter, radius of circle
#Output: return area of circle
def circArea(radius):
    area = math.pi * radius ** 2
    return area

#Input: paramters: length and width
#Output: returns area of a rectangle
def rectArea(length, width):
    area = length * width
    return area

def outputValue(area):
    print("Area: " + str(area) + "\n")

    
def main():

##    bananaSong("Katie")
##
##    names = ["Brandi", "Sean", "Megan", "Denkyiri"]
##
##    for studentName in names:
##        bananaSong(studentName)
##        print()
##
##    ans1 = addTwo(4, 5)
##    ans2 = addTwo(7, -3)
##    ans3 = addTwo(5, 10)
##
##    print()
##    for i in range(ans1):
##        print("hi")

    area = circArea(10)
    outputValue(area)

    area = circArea(3)
    outputValue(area)

    area = rectArea(3, 5)
    outputValue(area)

    area = rectArea(8, 10)
    outputValue(area)

    area = rectArea(6, 4)
    outputValue(area)
main()
