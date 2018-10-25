def userName():
##    sent= "This is and EXampLE. Ron, do you like it?"
##    sent.split()
##    print(sent)
    
    name= input("enter your full name: ")

    #variablename.function()

    nameList=name.split()

    #nameList=["Tyler","Patrick", "Montgomery"]
    first= nameList[0] #string
    middle=nameList[1] #string
    last=nameList[2] #string

    ##slicing with :

    userName=first[0]+middle[0]+last[:8]
    userName=userName.lower()
    email=userName + "@g.cofc.edu"
    print("\nUsername is: " + userName)
    print("Email: " +email)
    

def date():
    months=["Jan", "Feb", "Mar" ,"Apr","Jun","May","Jul","Aug","September","Oct","Nov","Dec"]
    date=input("Enter date in for mm/dd/yyyy: ")
    dateList=date.split("/")
    print("dateList: ", dateList)

    monthNum=int(dateList[0])
    print(months[monthNum-1])

    longDate = months[monthNum-1]+ " " + dateList[1] + ", " + dateList[2]
    print("'\nDate is: " + longDate)

def kindOfFile():
    fileContacts="Alex\nSpencer\nMeagan\nJack"
    print(fileContacts)
    lines=fineContacts.split()
    print(lines)


    ##name=zach
    ##name.center(20)
    ##'         Zach        '

    ##fileContacts use this list
    ##"..".join(fileContacts)
    ##Alex..Spencer..Meagan..Jack
    ##names=" ".join(fileContacts)
    ##print(name)
    ##Alex, Spencer, Meagan, Jack

    ##name=Shefalli Emanuel
    ##name.replace("m", "mm")
    ##Shefalli Emmanuel

    ##name=Shefalli Emmanuel
    ##name.find("e")
    ##2   (gives back index postion of first occurence in that string)
    ##name.find("m")

    ##name.count("z")
    ##0

    ##name.find("z")
    ##-1
    ##9

    def readFileEx():
    ##line is a string
        infile = open("date.txt","r")
##        for line in infile:
##            print(line)
        for line in infile:
            firstInitial=line[0]
            print(firstInitial)
            lastInitial=line[-2]
            print(lastInitial)

        print("done")
