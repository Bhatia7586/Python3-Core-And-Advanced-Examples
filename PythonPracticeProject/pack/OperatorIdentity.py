#!/usr/bin/python

a = 100
b = 100

if ( a is b ):
    print(" Identity Operators : a and b have same identity")

if ( id(a) == id(b) ):
    print(" Identity Operators : a and b have same identity")

b = 300
if ( a is b ):
    print(" Identity Operators : a and b have same identity")
else:
    print(" Identity Operators : a and b do not have same identity")

if ( a is not b ):
    print(" Identity Operators : a and b do not have same identity")
