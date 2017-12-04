class Person:
    personId=10
    
    #Constructor or Initializer
    def __init__(self, name):
        self.name=name
        
    def whoami(self):
        return "you are "+self.name
    
p1 = Person("SadaLearningHub")
print("Who am I: "+p1.whoami())
print("Name variable contains : ",p1.name)
p1.name = "Gopi"
print("Who am I: "+p1.whoami())