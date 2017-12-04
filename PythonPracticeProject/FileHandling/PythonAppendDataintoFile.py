

#opening the file
#r - read
#w - write
#a - append
#wb - write binary data
#rb - read binary data
f=open("File1.txt","a")
print("File is opend")

#appending data into file
f.write("This is my thired line\n")
print("data is appended")

#Closeing the file
f.close()
print("File Closed")


