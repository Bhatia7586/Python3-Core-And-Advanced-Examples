#open the file
f=open("File1.txt","r")
print("File is opened")

#read the data from file using for loop
print("--------------------")
for line in f:
    print(line)
print("--------------------")
print("Reading is complted")


#close the file
f.close()
