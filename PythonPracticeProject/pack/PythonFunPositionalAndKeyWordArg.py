def named_args(name,greeting):
    print(greeting+" "+name)
    
    
named_args("sadalearninghub", "Welcome to") #Positional Arguments

named_args(name="sadalearninghub", greeting="Welcome to") #Keyword arguments

named_args(greeting="Welcome to",name="sadalearninghub") #Keyword arguments


def my_func(a,b,c):
    print(a,b,c)
    
my_func(1,2,3) #Positional arguments

my_func(1,b=2, c=3) #Mixing positional and keyword arguments

my_func(1,c=3, b=2) #Mixing positional and keyword arguments

my_func(1,b=2,c=3)
