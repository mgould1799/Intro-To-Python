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
            
    

def main():
    for i in range(5):
        nums=[]
        for i in range(10):
            nums.append(random.randint(20,50))
        minimum=findMin(nums)
        print(nums)
        print("min: " +str(minimum))

    grades= [91,90,89.99,81,80,79,71,70,69,61,60,59]
    for grade in grades:
        print(grade,": ", letterGrade(grade))

main()
