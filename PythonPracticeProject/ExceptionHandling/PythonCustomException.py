import ExceptionHandling.NegativeAgeException

def enterage(age):
    if age<0:
        raise ExceptionHandling.NegativeAgeException("only positive integers are allowed")
    
    if age%2==0:
        print("age is even")
    else:
        print("age is odd")
        
try:
    num = int(input("Enter age :"))
    enterage(num)
except ExceptionHandling.NegativeAgeException:
    print("only positive integers are allowed")
except:
    print("Something is wrong")