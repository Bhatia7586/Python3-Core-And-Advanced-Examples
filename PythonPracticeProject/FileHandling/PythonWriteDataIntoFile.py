#open the file
f = open('File1.txt','a')
if f!=None:
    print("File is opened")
    f.write('this is my first line\n')
    f.write('this is my second line\n')
    print("data written done")
    
#closeing the file
f.close()
print("File is successfully closed")