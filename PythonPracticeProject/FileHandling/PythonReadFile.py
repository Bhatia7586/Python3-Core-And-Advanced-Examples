
#opening file
f = open("File1.txt","r")
#reading data from file
data = f.read()
print(data)
#closeing the file
f.close()
print("=========================================")


#opening file
f = open("File1.txt","r")
#reading data from file
data = f.readlines()
print(data)
for line in data:
    print(line)
#closeing the file
f.close()
print("===================================")


#opening file
f = open("File1.txt","r")
#reading data from file
data = f.readline()
print(data)
#closeing the file
f.close()

