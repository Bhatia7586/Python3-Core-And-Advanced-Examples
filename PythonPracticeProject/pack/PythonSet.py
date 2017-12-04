#Create a set in Python:
#A new empty set
setx = set()
print(setx)
#A non empty set
n = set([0, 1, 2, 3, 4, 5])
print(n)


#Iteration Over Sets:
num_set = set([0, 1, 2, 3, 4, 5])
for n in num_set:
    print(n)
    
#Add member(s) in Python set
#A new empty set
color_set = set()
#Add a single member
color_set.add("Red")
print(color_set)
#Add multiple items
color_set.update(["Blue", "Green"])
print(color_set)


#Remove item(s) from Python set:
#pop() function:
num_set = set([0, 1, 2, 3, 4, 5])
num_set.pop()
print(num_set)
num_set.pop()
print(num_set)
#remove() function:
num_set = set([0, 1, 2, 3, 4, 5])
num_set.remove(0)
print(num_set)
#discard() function:
num_set = set([0, 1, 2, 3, 4, 5])
num_set.discard(3)
print(num_set)



#Intersection of sets:
#Intersection
setx = set(["green", "blue"])
sety = set(["blue", "yellow"])
setz = setx & sety
print(setz)


#Union of sets:
#Union
setx = set(["green", "blue"])
sety = set(["blue", "yellow"])
seta = setx | sety
print (seta)


#Set difference:
setx = set(["green", "blue"])
sety = set(["blue", "yellow"])
setz = setx & sety
print(setz)
setb = setx - setz
print(setb)


#Symmetric difference:
setx = set(["green", "blue"])
sety = set(["blue", "yellow"])
setc = setx ^ sety
print(setc) 


#issubset and issuperset:
setx = set(["green", "blue"])
sety = set(["blue", "yellow"])
issubset = setx <= sety
print(issubset)
issuperset = setx >= sety
print(issuperset)


#More Example:
setx = set(["green", "blue"])
sety = set(["blue", "green"])
issubset = setx <= sety
print(issubset)
issuperset = setx >= sety
print(issuperset)

#Shallow copy of sets:
setx = set(["green", "blue"])
sety = set(["blue", "green"])
setd = setx.copy()
print(setd)

#Clear sets:
setx = set(["green", "blue"])
sete = setx.copy()
sete.clear()
print(sete)


