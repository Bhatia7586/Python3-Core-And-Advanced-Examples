#!/usr/bin/python


#find the prime numbers from 2 to 100
a = 2
while(a < 100):
    b = 2
    while(b <= (a/b)):
        if not(a%b): break
        b = b + 1
    if (b > a/b) : print (a, " is prime")
    a = a + 1

