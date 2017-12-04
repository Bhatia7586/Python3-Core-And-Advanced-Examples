global_var = 12 #this is global variablr
def func():
    local_var=100 #this is localvarible
    print("checking the scope of local and global variable in function")
    print("Local variable value",local_var)
    print("Global variable value",global_var)
    print("-----------------------------------")
    
print("checking the scope of local and global variable in out side of function")
#print("Local variable value",local_var)
print("Global variable value",global_var)
print("-----------------------------------")

func()


xy="Here xy is Global variable"
def cool():
    xy="Here XY is Local variable"
    print(xy)
    
cool()
print(xy)


t=1
def increment():
    global t #now t insidethe function is same as t outside the function
    t=t+1
    print("with in the function t value is :", t)
    
increment()
print("with in the out side of the function t value is :", t)
