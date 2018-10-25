

import random
##practice test april 2015 number 3
def cellCount(wbc,rbc):
    if 4500<wbc<11000 and 3.5<rbc<5 :
        results = "normal"
    else:
        
        if wbc > 11000 or rbc > 5:
                results= "high"
        else:
                results="low"
                
    return results
##practice test april 2015 number 5
def legitValuePos(nums):
    try:
        number=random.randint(50,100)
        pos=nums.index(number)
    except ValueError:
        pos=-1
    print(number ,"is at: " ,pos)

##practice test november 2013 num 2
def bloodPressure(s,d):
    if s<120 or d>80:
        results="normal"
    else:
        if(s<=120 and s>=139) or (d<=80 or d>=89):
            results="prehyper"
        else:
            results="high"
    return results

def index(items,value):
    try:
        pos=items.index(value)
    except ValueError:
        pos=-1
    print(value," is found at ",pos)
    

#practice test april 2015 num 4
def password():
    password=input("enter a password between 8 and 14 characters and it cant start with * : ")
    while len(password)<=8 or len(password)>=14 or password[0]=="*":
        password=input("enter a password between 8 and 14 characters and it cant start with * : ")
    return password

def password2():
    pw=input("enter a pw longer than 6 characters and ends with ! or starts with ab: ")
    while pw[-1]!="!" or pw[0:2]!="ab" and len(pw)!=6:
        pw=input("enter a pw longer than 6 characters and ends with ! or starts with ab: ")
    return pw
def alter2(values):
    newValue=[]
    for value in values:
        newValue.append(value)
    newValue.sort()
    newValue.reverse()
        

def main():
    results1= cellCount(5000,4)
    print("results one is: " + results1)
    results2=cellCount(4200,3)
    print("results two is: " + results2)
    results3=cellCount(12000,6)
    print("results 3 is: " + results3)

    list1=[]
    for i in range(50,100):
        list1.append(i)
    print(list1)
    prime=legitValuePos(list1)

    b1=bloodPressure(120,80)
    print("result 1 is: "+b1)
    b2=bloodPressure(150,95)
    print("result 2 is: "+b2)
    b3=bloodPressure(122,83)
    print("result 3 is: "+b3)
    

    values=[1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,16,16,0]
    val=16
    prime5=index(values,val)
    print(prime5)
    prime6=index(values,17)
    print(prime6)
    prime7=index(values,3)
    print(prime7)
    print(values)
    values.sort()
    print(values)
    values.reverse()
    print(values)

    values2=[3,5,7]
    alter2(values2)
    print(values2)

    nameList=[]
    name=input("enter a name: ")
    while name!="":
        nameList.append(name)
        name=input("enter a signle name: ")
    nameList.sort()
    nameList.reverse()
    print(nameList)
    
    

main()
