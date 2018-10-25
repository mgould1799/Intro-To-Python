import random
##input: parameter numeric grade
#output: returns letter based on grade
def letterGrade(grade):
    if grade >=90:
        letter = "A"
    elif grade >=60 and grade<70:#(this added to make better)
        letter="D"
## the d placed here causes a logic problem between b and c 
    elif grade >= 80:
        letter="B"
    elif grade >=70:
        letter = "C"
##    elif grade >=60:
##        letter="D"
    else:
        letter="F"
    return letter
##    if grade >=90:
##        letter="A"
##    else:
##        if grade >=80:
##            letter="B"
##        else:
##            if grade >=70:
##                letter="C"


#input: paramter list of numbers
#output: return the smallest num in list
#let min be first element in list.
#for every other value in list:
#   compare to min
#   if value<min:
#       adjust min
#insertion algorithm
def findMin(nums):
    minVal=nums[0]
    for i in range(1,len(nums)):
        if nums[i]<minVal:
            minVal=nums[i]
    return minVal


#minPos=0
#let min be the first element in the list
#for every other value in list:
#   compare val to min
#   if val < nums[minPos]:
#       adjustPos
#inputL parameter list of nums
#output:return position of smallest num in list 
def findMinPos(nums):
    minPos=0
    for i in range(1,len(nums)):
        if nums[i]<nums[minPos]:
            minPos=i
    return minPos
##min position can make changes to a list much easier. min cant do much


#(rect, clickPt) will allow you be able to determine if someone clicked in it
#rect p1=(50,90)
#rect p2= (70,100)
#click Pt1=(60,95) follows in rect because x and y is between rect x and ys
#clickPt2=(80,95) no 
#clickPt3=(60,50) no
# didClick(rect,pt)->boolean
    

def main():
    print("find min")
    for i in range(5):
        nums=[]
        for i in range(10):
            nums.append(random.randint(20,50))
        minimum=findMin(nums)
        print(nums)
        print("min: " +str(minimum))
    print()

    print("findMinPos")
    for i in range(5):
        nums=[]
        for i in range(10):
            nums.append(random.randint(20,50))
            minimum=findMinPos(nums)
        print(nums)
        print("pos: " +str(minimum))
    print()

    print(findMin([5,10,7,9]))

    print()
    print("letterGrade")
    grades= [91,90,89.99,81,80,79,71,70,69,61,60,59]
    for grade in grades:
        print(grade,": ", letterGrade(grade))

main()
