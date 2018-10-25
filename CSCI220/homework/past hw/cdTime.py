##Name: Meagan Gould
##Problem: This program will help find the total time of tracks on a CD that are inputed
##Certification of Authenticity: I certify that this lab is entirely my own work.
## I did discuss this program with Shefalli and Megan. 

def cdTime():
    print("This program will help you figure out how much time is on multiple CDs")

    
    ##Input: Number of CDs and tracks. The number of minutes and seconds on each track. From user
    ##Totals for CD, Min, and Sec
    totalMin= 0
    totalSec = 0
    numCDs= eval(input("Enter how many CDs you are trying to find out the time for: ")) 

    ##loop for the number of CDs
    for j in range(numCDs):
        
        ##find out how many tracks are on CDs
        numTracks= eval(input("Enter how many tracks are on CD# " + str(j + 1) +": "))
        
        ##loop to find out mins and secs
        for i in range (numTracks):
            numMinutes = eval(input("Enter how many minutes for this track: "))
            numSeconds = eval(input("Enter how many seconds for this track: "))
            print()
            
            ##equations to find mins and secs
            totalMin= totalMin +numMinutes 
            totalSec = totalSec + numSeconds
            
            ##convert mins and secs to make total mins
            totalMin2 = (totalSec//60) + totalMin
            
            ##the secs are converted to remainder to give total secs
            totalSec= totalSec%60
            ##print total times in mins and secs
            
            print("CD#" + str(j+1)+ ": " + str(totalMin2)+ " minutes " + str(totalSec)+ " seconds ")
            print()

            
    ##equations to figure out hours, mins, and secs
    totalHour = (totalMin // 60)
    totalMin2 = (totalSec//60) + totalMin
    totalMin =  totalMin%60
    totalSec= totalSec%60

    
    ##Output: Total hours, minutes, and seconds. All printed to the monitor. 
    print("Total time: ", totalHour, "hours", end = " ")
    print(totalMin, "minutes", end=" ")
    print(totalSec, "seconds", end =" ")
    print()

def total():
        total=0
        for i in range(5):
            total = total + i
            print(i)
