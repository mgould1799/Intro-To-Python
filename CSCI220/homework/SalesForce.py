from SalesPerson import *

class SalesForce:

    def __init__(self):
        self.salesList=[]

    def addData(self,fileName):
        infile=Open(fileName,"r")
        print(infile)
        for line in infile:
            #figure out what to append
            split=line.split()
            ID=split[0]
            name=[1]+[2]
            print(split)
            sales=[3]
            person=salesPerson(ID,name)
            person.enterSale(sale)
            self.salesList.append(person)
            
            

    def quotaReport(quota):
        for person in self.salesList:
            print(person)
            quotaMet=self.saleslist.metQuota(quota)
            print(quotaMet)

    #def topSalesPerson():

    def individualSales(ID):
        try:
            salesListIndex=self.salesList.index(ID)
            sales=salesListIndex.getSales()
            total=salesListIndex.totalSales()
            print(ID+"number of sales: " + str(sales) + " and total number of sales: "+str(total))
    
        except ValueError:
            print("that ID number is not in there.")

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


            


            

    
        
        
