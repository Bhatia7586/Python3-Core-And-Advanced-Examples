try:
    fh = open("TestFile.txt","w")
    print("File is opened")
    fh.write("This is my test file for exception handling")
    
##except with single argument
except IOError:
    print("Error: can not find the file or read data")
    
##except with zero argument
#except:
#    print("Error: can not find the file or read data")
    
##except with multiple arguments
#except (Exception1[,Exception2[,...ExceptionN]]):

else:
    print("Written content in the file successfully")
    fh.close()
    