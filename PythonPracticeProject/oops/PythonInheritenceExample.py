class Vehicle:
    def __init__(self, name,color):
        self.__name=name
        self.__color = color
    
    def getColor(self):
        return self.__color
    
    def setColor(self,color):
        self.__color = color
        
    def getName(self):
        return self.__name
    
    
    
class Car(Vehicle):
    def __init__(self,name,color,model):
        super().__init__(name,color)
        self.__model=model
        
    def getDescription(self):
        return self.getName()+self.__model+" in "+self.getColor()+" Color"
    
    
c=Car("Ford","Black","Abc123")
print("Description of the car is: ",c.getDescription())
print("Name of the car : ",c.getName())
    