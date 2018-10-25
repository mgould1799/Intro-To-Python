import math
class Circle:
    def __init__(self, X,Y,radius,center):
        self.X=X
        self.Y=Y
        self.radius= radius
        self.center=center

    #getter method
    def getCenter(self):
        return self.getCenter

    def getRadius(self):
        return self.getRadius

    #setter methods
    def setCenter(self,X,Y):
        if type(X)==int and type(Y)==int:
            self.setCenter=(X,Y)
    def setRadius(self,radius):
        if type(radius)==int:
            self.setRadius=radius

    def getArea(self, radius):
        if type(radius)==int:
            self.getArea=math.pi*(radius**2)
            
    #str methods

    #def __str__(self):
        
        
    
