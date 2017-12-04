
try:
    number = eval(input("Enter a number : "))
    print("The number u are entered is : ", number)
except NameError as ex:
    print("Exception is :", ex)