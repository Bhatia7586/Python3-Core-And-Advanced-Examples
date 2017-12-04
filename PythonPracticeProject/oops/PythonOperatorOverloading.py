import math

class Circle:
    def __init__(self,radius):
        self.__radius = radius
        
    def setRadius(self,radius):
        self.__radius = radius
        
    def getRadius(self):
        return self.__radius;
    
    def area(self):
        return math.pi*self.__radius**2
    
    def __add__(self,another_circle):
        return Circle(self.__radius+another_circle.__radius)
    
    def __gt__(self,another_circle):
        return self.__radius>another_circle.__radius
    
c1 = Circle(4)
print("Radius of circle c1 is : ",c1.getRadius())

c2 = Circle(5)
print("Radius of circle c2 is : ",c2.getRadius())

c3 = c1+c2
print("Radius of c3 Circle is : ",c3.getRadius())

print("checking operator overloading on grater than :", c3>c1)