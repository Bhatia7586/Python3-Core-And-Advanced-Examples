#!/usr/bin/python

'''Syntax of Nested If : 
if expression1:
   statement(s)
   if expression2:
      statement(s)
   elif expression3:
      statement(s)
   else:
      statement(s)
elif expression4:
   statement(s)
else:
   statement(s)
'''
var = 500
if var < 600:
    print("Expression value is less than 300")
    if var == 160:
        print("Which is 160")
    elif var == 500:
        print("Which is 500")
    elif var == 60:
        print("Which is 60")
else:
    print("Could not find true expression ie else statement")

