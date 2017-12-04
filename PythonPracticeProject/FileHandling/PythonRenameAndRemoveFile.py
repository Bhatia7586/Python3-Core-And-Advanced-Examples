import os

#Rename a file from File1.txt to File3.txt
os.rename("File3.txt","TextFile.txt")
print("File is renamed to File3.txt to TextFile.txt done")

#Delete file File2.txt
os.remove("TextFile.txt")
print("TextFile.txt is deleted")