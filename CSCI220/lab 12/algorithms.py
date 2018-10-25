from graphics import *
#lab 12
#Name:Meagan Gould

##comments on binary and linear search
##  the binary search seemed to go faster when sorting through a huge list of items
##  the linear search seemed to go faster when sorting through a short list


##code you make is much slower than python because the complexity is worse case o(n**2)
##python uses O(nlogn) which is alot less


def reverseSort(list1):
    newList=[]
    for names in list1:
        newList.append(names.lower())
    
    newList.sort()
    newList.reverse()
    print(newList)

def findAndRemoveFirst(list1,value):
    index=list1.index(value)
    #list1.remove(value)
    list1.pop(index)
    list1.insert(index,"Meagan")
    
    print(list1)

def readData(filename):
    infile=open(filename,"r")
    readFile=infile.read()
    list2=readFile.split()
   
    for i in range(len(list2)):
        list2[i]=eval(list2[i])
    
    return list2

def isInLinear(searchVal,values):
    i=0
    result=False
    while i<len(values) and values[i]!=searchVal:
        
        i+=1
    if i!=len(values):
        result=True
        
    
    return result

def isInBinary(searchVal,values):
    low=0
    high=len(values)-1
    mid=(low+high)//2
    
    while low<=high and values[mid]!=searchVal:
        if searchVal< values[mid]:
            high=mid-1
        else:
            low=mid+1
        mid=(low+high)//2
    if low<=high:
        found=True
            
            
    else:
        found=False
            
            
        
    return found

def selectionSort(values):
    n=len(values)

    for front in range(n-1):
        minPos=front
        for i in range(front+1,n):
            if values[i]<values[minPos]:
                minPos=i
        tempPos=values[minPos]
        values[minPos]=values[front]
        values[front]=tempPos

def rectArea(rectangle):
    p1=rectangle.getP1()
    p2=rectanle.getP2()
    x1=p1.getX()
    x2=p2.getX()
    y1=p1.getY()
    y2=p2.getY()
    height=abs(x1-x2)
    width=abs(y1-y2)
    
    return height*width
    
    
def rectSort(rectangles):
    n=len(values)

    for front in range(n-1):
        minPos=front
        for i in range(front+1,n):
            if values[i]<values[minPos]:
                minPos=i
        tempPos=values[minPos]
        values[minPos]=values[front]
        values[front]=tempPos

    

    
    

def main():
    list1=["Blue", "red","Green", "change","Apple","ab","Zebra","zayn"]
##    print(list1)
##    reverseSort(list1)
##    Green="Green"
##    print(list1)
##    findAndRemoveFirst(list1,Green)
##    print(list1)
##    findAndRemoveFirst(list1,"Turkey")
##    print(list1)

    run=readData("dataSorted.txt")
    print(run)

    search=isInLinear(5,run)
    print(search)
    search2=isInLinear(1000,run)
    print(search2)

    search3=isInBinary(5,run)
    print(search3)
    search4=isInBinary(282,run)
    print(search4)


    values=[5, 9,30,1,40]
    print(values)
    selectionSort(values)
    print(values)



    rect=Rectangle(Point(20,50),Point(50,90))
    area=rectArea(rect)
    print(area)
main()
