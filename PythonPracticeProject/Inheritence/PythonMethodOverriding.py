class A():
    def __init__(self):
        self.__x = 1
        
    def m1(self):
        print("m1 method from A Class")
        
class B(A):
    def __init__(self):
        self.__y = 1
        
    def m1(self):
        print("m1 method from B class")
        
b1 = B()
b1.m1()

print(isinstance(b1, B))
print(isinstance(1.2, int))