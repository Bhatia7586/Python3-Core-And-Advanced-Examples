import pickle

#opening the File
f=open("File2.dat","rb")
print("Binary file is opened")

#reading the data from binary file
print(pickle.load(f))
print(pickle.load(f))
print(pickle.load(f))
print("Reading is done")


#Closing the file
f.close()
print("file is closed")