#class practice problem

class GasPump:
    def __init__(self):
        self.cost=0
        self.numGallons=0

    def setCost(self,cost):
        if (type(cost)==int or type(cost)==float) and cost>0:
            self.cost=cost

    def setNumGallons(self,gallons):
        if (type(gallons)==int or type(gallons)==float) and gallons>0:
            self.numGallons=gallons

    def getCost(self):
        return self.cost
    def getNumGallons(self):
        return self.numGallons

    def dispenseFuel(self,amount):
        if amount<=self.numGallons:
            self.numGallons-=amount
            cost=amount*self.cost
        else:
            cost=0
        return cost

    def __str__(self):
        returnStr="Gallons available: " +str(self.numGallons)
        returnStr+="Price per gallon: ${0:.2f}".format(self.cost)

class GasStation:
    def __init__(self):
        self.pumps=[]

    def addPump(self,gallons,cost):
        pump=GasPump()
        pump.setNumGallons(gallons)
        pump.setCost(cost)
        self.pumps.append(pump)

    def sort(self):
        n=len(self.pumps)
        for front in range(n-1):
            mp=front
            for i in range(front+1,n):
                if self.pumps[i].getNumGallons()<self.pumps[mp].getNumGallons():
                    mp=i
            temp=self.pumps[front]
            self.pumps[front]=self.pumps[mp]
            self.pumps[mp]=temp

    def __str__(self):
        returnStr=""
        for pump in self.pumps:
            returnStr+=pump
        return returnStr


def main():
    shell=GasStation()
    shell.addPump(50,3)
    shell.addPump(20,2.5)
    shell.addPump(70,2)
    shell.addPump(100,3)
    shell.addPump(15,2)

    print(shell)
    shell.sort()
    print(shell)
    
##    pump=GasPump()
##    pump.setNumGallons(50)
##    pump.setCost(2.37)
##    print(pump)
##    print(pump.getCost())
##
##
##    print("4.7 gall: ",pump.dispenseFuel(4.7))
##    print()
##    print(pump)
##    print("20 gall: ",pump.dispenseFuel(20))
##    print()
##    print(pump)
##    #print(pump)
##    print("30 gall: ",pump.dispenseFuel(30))
##    print()
##    print(pump)
main()

#software development process
#1)understand what problem is asking
#2)deteremine specifications: info coming and what is return
#3)desgin the code: diagram or  sudocode
#4)implement the code
#5)test and debugg
#6) maintain the code
