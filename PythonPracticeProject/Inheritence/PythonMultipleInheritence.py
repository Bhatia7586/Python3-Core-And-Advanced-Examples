class MySuperClass1():
    def method_super1(self):
        print("method_super1 method called")
        
        
class MySuperClass2():
    def method_super2(self):
        print("method_super2 method called")
        
        
class ChildClass(MySuperClass1, MySuperClass2):
    def child_method(self):
        print("This is child method")
        
        
c = ChildClass()
c.child_method()
c.method_super1()
c.method_super2()