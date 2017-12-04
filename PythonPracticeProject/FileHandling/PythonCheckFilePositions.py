
#opening the File
fo = open("File1.txt", "r+")
str = fo.read(10)
print("Read String is : ", str)

#Checking the current position
position = fo.tell()
print("Current position of the file is:",position)

#Reposition  pointer at the begining of the file
position = fo.seek(0,0)
str= fo.read(10)
print("Again read string is:", str)

#Close the file
fo.close()




