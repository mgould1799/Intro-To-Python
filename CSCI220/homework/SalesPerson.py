#Name:Meagan Gould


class SalesPerson:

    def __init__(self,ID,name):
        self.ID=ID
        self.name=name
        self.sales=[]

    #getter
    def getID(self):
        return self.ID

    def getName(self):
        return self.name

    def getSales(self):
        return self.sales

    #setter
    def setName(self,name):
        if type(name)==str:
            self.Name=name
    def setID(self,ID):
        if type(ID)==int:
            self.ID=ID

    #other programs

    def enterSale(self,aSale):
        if type(aSale)==int or type(aSale)==float:
            self.sales.append(aSale)

    def totalSales(self):
        totalSale=0
        for i in range(len(self.sales)):
            totalSale+=self.sales[i]
        return totalSale
    
        

    def metQuota(self,quota):
        if quota>=self.totalSales():
            met=False
        else:
            met=True
        return met

    def compareTo(self,otherPerson):
        if self.totalSales()>otherPerson.totalSales():
            value=1
        elif self.totalSales()<otherPerson.totalSales():
            value=-1
        elif self.totalSales()==otherPerson.totalSales():
            value=0
        return value

    #str
    def __str__(self):
        display= "ID: "+str(self.ID)+ " Name: "+str(self.name)+ " Total Sales: "+ str(self.totalSales())
        return display
        
        
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

main()
    
