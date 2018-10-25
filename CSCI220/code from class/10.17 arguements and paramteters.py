import math
##input:radius of circle,parameter
## output: return the area of a circle

def circArea(rad):
    area= math.pi* rad**2
    return area


##input: length and width of a rect, parameters
##output: return area of rect
def rectArea(length,width):
    area= length * width
    return area

##Input: list of numbers, paramters
##output: return aver of the numbers
def calcAverage(nums):
    total = 0
    for num in nums:
        total+=num
    avg=total/len(nums)
    return avg

##void function- does not return a value
##input: list of nums and name of output file, parmeter
##Output: writes average of numbers to output file
def writeAverage(nums, filename):
    total = 0
    for num in nums:
        total+= num
    avg=total/len(nums)
    outfile= open(filename,"w")
    print(avg,file=outfile)
    outfile.close()

##input: list of values and a single value, parameters
##Output: nothing, but a single value is appended to the list
#void function
def changeList(values ,value):
    values.append(value)
    

def main():
    print(circArea(10))

    area= circArea(3)
    print("area of rad = 3" + str(area))

    aArea= rectArea(3,5)
    print("Area of l=3,w=5: " +str(aArea))

    rArea=rectArea(4,6)
    print("Area of l=4, w=6 : " +str(rArea))
    ##4 and 6 arguement here . 4 is passed to parameter of length

    average= calcAverage([3,5,7])
    print(str(average))
    ##list is arguement
    ##paramter is the nums

    average = calcAverage([70,80,90,100,100])
    print(str(average))

##    writeAverage([3,5,7],"avg.txt")
##    print("data written to: " + filename)

    names= ["Alex", "Jace", "Meagan"]
    print(names)
    changeList(names,"Matt")
    print(names)

    #values = names *values is an alias for names
    
main()

##arguement- value passed to paramter
## parameter -variable set a side in the fucntion header
##void function does not return anything ** can only print a message or just
    ## just changes a file, etc.

##fucntions allow for reuse
##removes redundancy (redundancy can cause error: which one is right?)
##only have to text one fucntion and ease in debugging


