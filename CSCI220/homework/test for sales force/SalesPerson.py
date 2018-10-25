#Name:Meagan Gould
#purpose:a program to create a class system for a salesperson and create a
#   a sales force from it
#Certification of Authenticity: I certify that this is my own work.
#i combines salesperson and salesforce in the same file


#creates the salesperson class
class SalesPerson:

    #creates the main function for salesperson
    #input:ID and name of salesperson
    #output:id, name, and a list of their sales
    def __init__(self,ID,name):
        self.ID=ID
        self.name=name
        self.sales=[]

    #getter

    #input:nothing
    #output:the id of the salesperosn
    def getID(self):
        return self.ID
    
    #input:nothing
    #output:the name of the salesperosn
    def getName(self):
        return self.name
    
    #input:nothing
    #output:the sales of the salesperosn
    def getSales(self):
        return self.sales

    #setter

    #input:name
    #output: changes the name of the salesperson
    def setName(self,name):
        if type(name)==str:
            self.Name=name
            
    #input:id
    #output: changes the id of the salesperson    
    def setID(self,ID):
        if type(ID)==int:
            self.ID=ID

    #other programs
        
    #input: a sale
    #output: the list of sales is added too
    def enterSale(self,aSale):
        if type(aSale)==int or type(aSale)==float:
            self.sales.append(aSale)

    #input: nothing
    #output: the total number of sales for the salesperson       
    def totalSales(self):
        totalSale=0
        for i in range(len(self.sales)):
            totalSale+=self.sales[i]
        return totalSale
    
        
    #input:quota
    #output: if the person met the quota or not
    def metQuota(self,quota):
        #see if quota was matched or not by if number of sales less or equal to quota
        if quota>=self.totalSales():
            met=False
        #else statement for if the salesperson was greater than the quota 
        else:
            met=True
        return met

    #input:another person
    #output:if the orginal salesperson sold more, sold less, or sold the same
    #   as the other salesperson
    def compareTo(self,otherPerson):
        #if orginal salesperson sold more or not
        if self.totalSales()>otherPerson.totalSales():
            value=1
        #if orginal salesperson sold less or not
        elif self.totalSales()<otherPerson.totalSales():
            value=-1
        #if orginal salesperson sold the same or not
        elif self.totalSales()==otherPerson.totalSales():
            value=0
        return value

    #str

    #input:nothing
    #output:id name and total sales of a salesperson
    def __str__(self):
        display= "ID: "+str(self.ID)+ " Name: "+str(self.name)+ " Total Sales: "+ str(self.totalSales())
        return display


#creates the sales force calass
class SalesForce:

    #creates the salesforce initinlizer
    #input:nothing
    #output:the sales list as a empty list 
    def __init__(self):
        #creates the salesforce list
        self.salesList=[]

    #input:a file name
    #output:adds the salesperson to the salesforce
    def addData(self,fileName):
        #rhs - changed below from Open to open
        #infile=Open(fileName,"r")

        #reads the file
        infile=open(fileName,"r")
        print(infile)
        for line in infile:
            #splits the file
            split=(line.split())
            #creates the id
            ID=split[0]
            #creates the name
            name=split[1]+split[2]
            #creates the salesperson
            person=SalesPerson(ID,name)
            #adds data to the sales person
            for i in range(3,len(split)):
                sales=float(split[i])
                enter=person.enterSale(sales)
            #appends the salesperson to the list 
            self.salesList.append(person)
            
            
    #input: quota
    #output: if a person met the quota or not
    def quotaReport(self,quota):
        #creates a loop to figure out if every person has met the quota or not
        for person in self.salesList:
            print(person)
            #function to see if they met quota or not
            quotaMet=person.metQuota(quota)
            print(quotaMet)

    #input: noting
    #output: the top sales person
    def topSalesPerson(self):
        #sets the user id 
        salesPerson=self.salesList[0]
        #creates the loop to compare the salesperson to the the first sales person
        for person in self.salesList:
            #see if they sold the same about
            if (salesPerson.compareTo(person)==0):
                top=person
            #see if they sold less
            elif(salesPerson.compareTo(person)==-1):
                top=person
        return top


        
        
            
    #input:ID
    #output: to figure if that id exists or not in a list 
    def individualSales(self,ID):
        #loops through all of the sales people
        for person in self.salesList:
            #gets the id 
            ID2=person.getID()
            #if statement to compare the two ids
            if float(ID)==float(ID2):
                    
                sales=" Number of Sales: " +str(person.getSales())
                total=" Total sales: "+str(person.totalSales())
                #print(total)
                #print(sales)
                print(str(ID)+sales+total)

            #else statement to tell if id is not in the loop
            else:
                print("that ID is not in there")

#rhs - dedented this
#main to test it
def main():
    theSalesForce = SalesForce()
    theSalesForce.addData("salesdata.txt")
    
    print ("Quota report:")
    theSalesForce.quotaReport(750)
    print ("\n************************\n")

    topSales = theSalesForce.topSalesPerson()
    print ("Top sales person:")
    print (topSales)
    print ("\n************************\n")
    
    theSalesForce.individualSales(123)
    print ()
    theSalesForce.individualSales(999)
    print ()
    theSalesForce.individualSales(456)
    print ()
    theSalesForce.individualSales(345)
main()
   
        
##def main():
##    sP = SalesPerson(1, "John")
##    sP.enterSale(10)
##    sP.enterSale(15)
##
##    print(sP.getSales())
##    print(sP.totalSales())
##    print(sP.metQuota(35))
##
##    sP2 = SalesPerson(2, "Carl")
##
##    print(sP.compareTo(sP2))
##
##    print(sP)
##    print(sP2)
##
###rhs  - commented this out...
##main()
    
