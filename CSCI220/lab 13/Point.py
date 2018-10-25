
#Name: Meagan Gould and Denkyiri

class Point:

    #constructor
    def __init__(self):
        self.X = 0 
        self.Y = 0

    #getter
    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    #setter
    def setX(self,X):
        if type(X)==int:
            self.X=X
    def setY(self,Y):
        if type(Y)==int:
            self.Y=Y

    #str method      
    def __str__(self):
##        return str(self.X) and str(self.Y)
        newX= str(self.X)
        newY= str(self.Y)
        return "(" + newX + ", "+ newY +")"
