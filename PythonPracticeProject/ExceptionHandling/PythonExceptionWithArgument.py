try:
    fh = open("TestFile1.txt","r")
    print("File is opened")
    fh.write("This is my test file for exception handling")
    
##except with single argument
except IOError:
    print("Error: can not find the file or read data")
    
    

finally:
    print("Finally block will execute all times")
    