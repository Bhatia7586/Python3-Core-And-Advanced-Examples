'''
Python support four different numerical types
1.int(signed integers)'''
intval = 10
print(intval)

'''2. long(long integers)'''
longval = 51924361L
print(longval)

'''3. float(floating point real values)'''
floatval = 15.20
print(floatval)

'''4. complex(complex number)
	are of the form a + bJ, where a and b are floats and J (or j) represents the square root of -1 (which is an imaginary number). The real part of the number is a, and the imaginary part is b. Complex numbers are not used much in Python programming.'''
complexval = 9.322e-36j
print(complexval)


''' Number Type Conversion : 
	1. int(x) 
	2. long(x) 
	3. float(x) 
	4.1. complex(x)
	4.2. complex(x, y)'''
#print(longval(intval))

'''Delete the reference to a number object :
		Syntax: del var1[,var2[,var3[....,varN]]]]'''
del intval
#print(intval

'''Determining Type : 
	Syntax : type(x)'''
print(type(floatval))
print(type(complexval))

