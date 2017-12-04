import os

#create a directory "SadaLearningHub"
os.mkdir("SadaLearningHub")
print("Directory is created with name called SadaLearningHub")

#Changing a directory to "/SadaLearningHub"
os.chdir("SadaLearningHub")
print("Changing the directory called SadaLearningHub")

#This would give location of the current dirctory
current_dir = os.getcwd()
print("Current Directory is : ", current_dir)

#Removing the directory
os.mkdir("test")
print("Subdirectory is created with name test")
os.rmdir("test")
print("test directory is removed")
