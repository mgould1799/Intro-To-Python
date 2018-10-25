def readFileEx():
    ##line is a string
        infile = open("date.txt","r")
##        for line in infile:
##            print(line)
        counter=1
        for line in infile:
            names=line.split()
            ##first=name[0]
            ##last=name[1]
            ##userName=(first[1]+last[0:4]).lower()
            ##userName+= str(len(last))
            userName=(names[0][1]+names[1][:4]).lower()
            userName+=str(len(names[1]))
            print(userName)
                        
            
##            firstInitial=line[0]
##            #print(firstInitial)
##            lastInitial=line[-2]
##            #print(lastInitial)
##            userName= (firstInitial+lastInitial).upper()
##            userName += str(counter)
##            print(userName)
##            counter+=1
        print("done")
def sumOfLines():
    infile=open("numData.txt", "r")
    grandTotal=0
    for line in infile:
        num=line.split()
        lineTotal=0
        for numStr in nums:
            lineTotal+= eval(numStr)
        grandTotal+=lineTotal
        print("Line total: " +str(lineTotal))
    print("Grand total: " +str(grandTotal))
    ##grandtotal = 0 
    ##output "1 2 3 \n"
    ## split line = list of str = ["1","2","3"]
    ##initialize line total
    ## for each num str in list : lineTotal +=eval(numStr)
    ##increase grandTotal by lineTotal
def Average():
        outfileName="averages.txt"
        infile=open("gradeForPerson.txt","r")
        outfile=open(outfileName, "w")
        for line in file:
                parts=line.split()
                ##["Evan","90","80","100"]
                grades=parts[1:]
                ##[90","80","100"]
        total = 0
        for gradeStr in grades:
                total+= eval(gradeStr)
        avg=total/len(grades)
        print(parts[0]+ ": "+ str(avg), file =outfile)
        print("Data written to: "+outfileName)
        ##tell where stuff went to 
    
##write to a file that does not exist. python creates a new one . do not over ride file   
