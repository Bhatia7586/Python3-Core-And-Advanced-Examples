a = 10
print("a value",a)

#Redeclaration of a
a = "SadaLearningHub"
print("a value", a)

#Multiple Assigniment
b=c=d="sada"
print("b value:",b," c value:",c," d value", d)

b,c,d=1,3,"SadaLearningHub"
print("b value:",b," c value:",c," d value", d)

print("Sadalearninghub"+str(100))


vara="Global"
print("Globle Variable", vara)
varc="SadaLearningHub"

def someFunction():
    print("Global varaible", varc)
    vara= "Local"
    varb="sada"
    print("Local varible varb :",varb)
    print("Local variable", vara)
   
someFunction()
print("Global varaible", vara)
print("Global varaible", varc)
#print("Local varible varb :",varb)

del a
#print(a)