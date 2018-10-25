import random
## val=[nums]
## total = 0
## for i in range(len(val)):  <-- initlizes value of i (i starts at 0)
##      total+= val[i]      #incriments i each iteration (i increased by 1)
##                          #makes sure i never exceeds the stop value(i less then len)

# while for have to deal with everything manually
##total=0
# i = 0
# while i < len(val):
##      total+= val[i]
##      i+=1

##val=[2,5,4,3,4]
# total                i                   val[i]
#   0                  0
#   2                  1                      2
#   7                  2                      5
#   11                 3                      4
#   14                 4                      3
#   18                 5                      4


#while loop that creates an average of the nums
def average(values):
    total=0
    i = 0
    while i < len(values):
        total+= values[i]
        i+= 1
    avg= total / len(values)
    return avg
## take away i and create an infinte loop

## totals nums up until total exceeds 100
## values = [30,40,50,5,7]
## stop: total > 100 or i < len(values)
## continue: not(total > 100 and i >= len(values))
## i           total           values[i]
## 0             0
## 1             30                30
## 2             70                40
## 3            120                50

def avg100(values):
    total = 0
    i = 0
    while not(total > 100 or i >= len(values)):
        total+= values[i]
        i=0
    return total/i

def main():

    print("average test")
    nums=[]
    for i in range(5):
        nums.append(random.randint(10,15))
    print(nums)

    ans= average(nums)
    print("Average: "+ str(ans))
    print()
    
    print("average test 100")
    nums2=[]
    for i in range(5):
        nums2.append(random.randint(30,50))
    print(nums2)
    
    ans2= avg100(nums2)
    print("Average: "+ str(ans2))
main()
