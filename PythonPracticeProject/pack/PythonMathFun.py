import math

'''round(number[, ndigits]) - rounds the number, you can also specify precision in the second argument'''
print(  'Round of the given number 2.1356871234 at 4th position : ', round(2.1356871234, 4)) # Return number with 3 digits after decimal point
print( 'Round of the 2.4 number : ', round(2.4))	

'''pow(a, b) - Returns a raise to the power of b'''
print( '4 raise to the power of 3 : ', pow(4, 3))

'''abs(x) - Return absolute value of x'''
print( 'Absolute value of the -22 is : ', abs(-22))

'''max(x1, x2,..., xn) - Returns largest value among supplied arguments'''
print( 'Maximum value of the 9, 4, 3 ,77 is : ', max(9, 4, 3 ,77))

'''min(x1, x2,..., xn) - Returns smallest value among supplied arguments'''
print( 'Minimum value of the 9, 4, 3 ,77 is : ', min(9, 4, 3 ,77))

'''ceil(x) - This function rounds the number up and returns its nearest integer'''
print( 'Ceil of the 2.13 is : ', math.ceil(2.13))

'''floor(x) - This function rounds the down up and returns its nearest integer'''
print( 'Floor of the 2.53 is : ', math.floor(2.53))

'''sqrt(x) - Returns the square root of the number'''
print( 'Square root of the number 25 is : ', math.sqrt(25))

'''sin(x) - Returns sin of x where x is in radian'''
print( '30 radian of the sin value is : ', math.sin(30))

'''cos(x) - Returns cosine of x where x is in radian'''
print( '30 radian of the cos value is : ', math.cos(30))

'''tan(x) - Returns tangent of x where x is in radian'''
print( '30 radian of the tan value is : ', math.tan(30))

