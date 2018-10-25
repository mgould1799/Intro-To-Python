from graphics import *

#in squared sorts- complexity is n**2. takes n**2 to sort the list


## 1 mil items 
##n*logn-> complexity of O(nlogn)-> 20 mil comparisons
##                      1 mil* 20
##n**2 sort-> complexity of 0(n**2)-> 1 trillion comparisons


##selection sort
# for front 0....n-1 = n timses 
#       find the position of the smallest element between front and n = n comparisons
#       swap smallest element with front of list

## 15 30 50 40 10 5 20
## 0   1 2  3   4 5 6
##front minpos i
## 0     0     1
##             2
#              3
#        4     4
#        5     5
#              6
#  1     1
#              2

#selection sort info
## temp=a
## a=b
## b=temp


##selection sort
# n=len(values)
## for front in range(n-1):
##      minPos=front
##      for i in range(front+1,n):
##          if values[i]<values[minPos]:
##              minPos=i
##          temp=values[minPos]
##          values[minPos]= values[front]
##          values[front]=temp



def selSort(values):
    n=len(values)

    for front in range(n-1):
        minPos=front
        for i in range(front+1,n):
            if values[i]<values[minPos]:
                minPos=i
        tempPos=values[minPos]
        values[minPos]=values[front]
        values[front]=tempPos

##selection sort to sort strings
def selSortStrings(words):
        n=len(words)

    for front in range(n-1):
        minPos=front
        for i in range(front+1,n):
            if words[i]<words[minPos].lower():
                minPos=i
        tempPos=words[minPos]
        words[minPos]=words[front]
        words[front]=tempPos

def selSortRadius(circles):
            n=len(circles)

    for front in range(n-1):
        minPos=front
        for i in range(front+1,n):
            if circles[i].getRadius()<circles[minPos].getRadius():
                minPos=i
        tempPos=values[minPos]
        values[minPos]=values[front]
        values[front]=tempPos
    
    
    
        
