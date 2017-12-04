#!/usr/bin/python

a = 50
b = 30
list = [100, 200, 300, 400, 500 ];

if ( a in list ):
    print("Membership Operators : a is available in the given list")
else:
    print("Membership Operators : a is not available in the given list")

if ( b not in list ):
    print("Membership Operators : b is not available in the given list")
else:
    print("Membership Operators : b is available in the given list")

a = 200
if ( a in list ):
    print("Membership Operators : a is available in the given list")
else:
    print("Membership Operators : a is not available in the given list")
