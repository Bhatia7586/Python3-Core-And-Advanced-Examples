import pickle

#opening the binary file
f=open("File2.dat","wb")
print("Binary file is opened")

pickle.dump(11,f)
pickle.dump("this is the text",f)
pickle.dump([23,42,30],f)
print("Writing data into Binary file is done")

#closing the file
f.close()
print("Binary file is closed")