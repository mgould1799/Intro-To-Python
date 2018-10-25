from SalesPerson import *

class SalesForce:

    def __init__(self):
        self.salesList=[]

    def addData(self,fileName):
        #rhs - changed below from Open to open
        #infile=Open(fileName,"r")
        infile=open(fileName,"r")
        print(infile)
        for line in infile:
            #figure out what to append
            split=(line.split())
            ID=split[0]
            name=split[1]+split[2]
        
            sales=split[3:]
            print(name)
            print(sales)
            person=salesPerson(ID,name)
            person.enterSale(sale)
            #print(person)
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

#rhs - dedented this
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


            


            

    
        
        
