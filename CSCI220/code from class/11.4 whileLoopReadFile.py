## DEMORGANS LAWS:
## not val == x -> val!=x
##not val > x = val <= x
## not val >= x = val < x
## not val < x = val >= x
## not val <= x = val > x
## not val!= x = val == x

## not(val > x and val <= Y)
## val <= x or val > y
## not not = nothing
## and = or
## or = and

## datefile.readline() -> one line of the file as a str
## search and find something within a list using a while loop
def readFile(filename, searchName):
    dateFile=open(filename)

    line= dataFile.readline()
    parts= line.split()
    name=parts[0]
    while line != "" and name!= searchName:
        line=dataFile.readline()
        if len(line) >0:
            parts= line.split()
            name=parts[0]
            
    if line == "":
        print(searchName+" not found")
    else:
        print(line)
        
    dataFile.close()

    
##enter a val until 57 because this makes it stop
## stop value== 57
##continue not (value == 57) = val != 57
def goodInput():
    value= eval(input("enter a num . 57 to stop: "))
    while value !=57:
        value= eval(input("enter a num . 57 to stop: "))
    print("you entered " + str(value))

##stop val==57 or value <0
## continue: not(value==57 or value <0)
##      value!= 57 and value >=0
def goodInput2():
    value= eval(input("enter a num . 57 to stop: "))
    while value !=57 and value >=0:
        value= eval(input("enter a num . 57 to stop: "))
    print("you entered " + str(value))

##stops at z and has more than 5 characters in it
def enterName():
    word= input("enter name with z word and has more than 5 letters: ")
    ##stop word[0]=="z" and len(word)>5
    ##continue not ^ --> word[0] != "z" or len(word) <=5
    while len(word) <=5 or word[0] !="z" :
       word= input("enter name with z word and has more than 5 letters: ")
    return word

##password has to have a ! and end withit and 6 or more characters
def checkPW():
    password=input("enter a pw that ends with ! and has more than 6 characters: ")
    ##stop:pwd[-1] == "!" and len(pwd) >= 6
    # continue: pwd[=1]!= "!" or len(password) < 6
    while len(password)>6 or password[-1] != "!":
        password=input("enter a pw that ends with ! and has more than 6 characters: ")
    return password
def main():
    print("good input test")
    goodInput()
    print()

    print("good input 2 test")
    goodInput2()
    print()

    print("enterName test")
    word= enterName()
    print("you entered " + word)
    print()

    print("check pw")
    pw= checkPW()
    print("you entered "+ pw)
    print()
    
    print("read file test")
    readFile("data.txt","grayson")
    
    
