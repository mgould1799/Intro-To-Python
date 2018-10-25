from graphics import *

#nums = [5,7,2]
#values= nums
#values.append(8)
#print(values) -> [5,7,2,8]
#print(nums)-> [5,7,2,8] ** this is because nums and values are now aliases

#name="Spencer"
#nickName=name
#name.lower() **this wont do anything
#name=name.lower() ** wont change anything because str are immutiable
## cant really have alias for str


##values= list of nums
#value= single item
#output- none
#purpose: to modify the list by appending value into values
def addValue(values,value):
    values.append(value)



def main():
    nums=[5,7,2]
    addValue(nums,8)
    print(nums)
    #values is an alias for nums because it is an object

#void function, name change color, 2 paramters(circle, string color)
def changeColor(circle, color):
    circle.setFill(color)

def main2():
    win=GraphWin("example",600,600)
    circPt=Point(300,300)
    circ= Circle(circPt,100)
    circ.setFill("blue")
    circ.draw(win)
    
    changeColor(circ,"purple")

##getGrades()-> list of grades: ask the user for the number of grades then build a list of all grades inputed by the user

def getGrades():
    numGrades=eval(input("enter num of grades: "))
    totalGrades=[]
    for i in range(numGrades):
        grades=eval(input("enter grade " +str(i+1)+":"))
        totalGrades.append(grades)
    return totalGrades
        
        
##averageGrades(grades)->float representing average of grades accepts a list of grades and return average of the list
def averageGrades(grades):
    #infile= open(grades, "r")
    fileSplit=grades.split()
    total=0
    for grades in gradeList:
        total+= grades
    avg=total/len(grades)
    return avg
        
    
##increaseScores(grades,adjustAmount)-> void function. accepts a list of grades and a curve amount and adjust each grades in the list by the curve amount
def increaseScores(grades,adjustAmount):
    for i in range(len(grades)):
        grades[i]+= adjustAmount
                   

def main3():
    grades =getGrades()
    print(grades)

    average =averageGrades(grades)
    print(average)

    increaseScores(grades,5)
    print("\nGrades after increase"+ str(grades))
    average
    
