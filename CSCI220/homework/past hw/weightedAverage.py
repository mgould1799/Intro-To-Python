#Name: Meagan Gould
#weightedAverage.py
##Purpose: to find the weighted average of grades witin a given set of data
##Input:data from a given list
##output: the weighted average onto the screen
##Authencity statement: I certify that this is my own work.
##I discussed this homework with Matt and Shefali. 



##reads file
def readFile(fileName):
    file=open(fileName,"r")
    avgTotal=0
    
    ##splits list and gets names
    avgTotal=0
    for grades in file.readlines():
        splitList = grades.split()
        names= splitList[0] + " "+ splitList[1]
        

        ##finds weight and grade and multiplies them together 
        total= 0
        for indexOfWeight in range(2, len(splitList),2):
            
            weight = int(splitList[indexOfWeight])
            grade = int(splitList[indexOfWeight+1])
            total+= weight*grade
            
        ##finds avg weight    
        avgWeight= total/100
        print("{0}'s average is: {1}".format(names, avgWeight))
        
    ##finding class average 
        avgTotal+= avgWeight
    avgOfClass= avgTotal/len(names)
    print()
    print("Class Average is: {0:0.1f}".format(avgOfClass))
        
        
            
##runs program in main and asks for data file             
def main():
    print("This program will help find the average grades stored in a file")
    print()
    fileName=str(input("Enter the name of the file storing the data for grades: "))
    print()
    readFile(fileName)
main()
            
        
    


    
