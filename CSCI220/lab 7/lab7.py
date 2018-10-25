# Lab7.py
# Name 1: Meagan Gould
# Name 2:Denkyiri Henderson


def numberWords():
    infile = open("rawWords.txt", "r")
    outfile=open("numberedWords.txt","w")
    fileR = infile.read()
    lineSplit= fileR.split()
    for i in range(len(lineSplit)):
       print(str(i+1)+ ". " +lineSplit[i], file = outfile)
    
       

def hourlyWages(infileName,outfileName):
    infile= open(infileName, "r")
    outfile = open(outfileName, "w")

    file = infile.readlines()

    for element in file:
        splitElement = element.split()
        firstName = splitElement[0]
        lastName = splitElement[1]
        hourWage = int(splitElement[2])
        hoursWorked = int(splitElement[3])
        newWage= hourWage+1.65
        total =  newWage*hoursWorked
    
        outfile.write(firstName + " " + lastName + " " + str(total) + "\n")
    print("Info was printed to: ", outfileName)
        
def nameValue(name):
    asii
    name= name.text()
    print(name)
        
    ord(name)
    
        
    
       
    
        
  
#main() should be the only file executed when you are checked off for this lab
#thus add code to main() to call any functions you write.
def main():
   numberWords()

   hourlyWages("hourlyWages.txt","wagesForWeek.txt")
    

main()

    
