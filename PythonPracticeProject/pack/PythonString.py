
'''Creating a string variable'''
str1 = 'SadaLearningHub Channel'
str2 = "Python Programming"
#==============================

'''Accessing values in Sting'''
print("zero index of the string : ", str1[0])
print('str1 String : ', str1)
print('characters from 1 to 5 index is: ', str1[1:5])
#==============================

'''Updating String'''
print("before updating string : ", str1)
print("After updating String : ", str1[:15] + ' Youtube Channel')
print("before updating string : ", str2)
print("After updating String : ", str2[0:5] + 'SadaLearningHub ')
#==============================

#'''Escape Characters
#	\a - Bell or alert
#	\b - Backspace
#	\cx - Control-x
#	\C-x - Control-x
#	\e - Escape
#	\f - Formfeed
#	\M-\C-x - Meta-Control-x
#	\n - Newline
#	\nnn - Octal notation, where n is in the range 0.7
#	\r - Carriage return
#	\s - Space
#	\t - Tab
#	\v - Vertical tab
#	\x - Character x
#	\xnn - Hexadecimal notation, where n is in the range 0.9, a.f, or A.F'''
#==========================================

'''String special operators : 
	+, *, [], [:], in , not in, %(Formating Operator)'''
x = 'SadaLearningHub '
y = 'Youtube Channel'
print('Concatination of two Strings : ', x + y)
print('Repetition of string : ', x*2)
print('slice of the string  : ', x[1])
print('Range Slice of the string : ', x[0:3])
print('Check Membership of the string : ', 's' in x)
print("My name is %s and weight is %d kg!" % ('Zara', 21))
'''	%c 	character
	%s 	string conversion via str() prior to formatting
	%i 	signed decimal integer
	%d 	signed decimal integer
	%u 	unsigned decimal integer
	%o 	octal integer
	%x 	hexadecimal integer (lowercase letters)
	%X 	hexadecimal integer (UPPERcase letters)
	%e 	exponential notation (with lowercase 'e')
	%E 	exponential notation (with UPPERcase 'E')
	%f 	floating point real number
	%g 	the shorter of %f and %e
	%G 	the shorter of %f and %E'''
#=======================================================

'''Triple Quotes         : '''
tripleQuoteStr = """This is the String for triple code example
it support the new lines [ \n ] and also supoort all special characters
 for example Tab space (\t)
"""
print(tripleQuoteStr)

print('http:\\sadalearninghub.com')
print(r'http:\\sadalearninghub.com')
#===========================================================

'''Unicode Example	 : 
	Normal strings in Python are stored internally as 8-bit ASCII. if you want to store unicode you need to use u in below line'''
print(u'SadaLearningHub')
#===========================================================

'''Operators on the String'''
print('sadalearning' + 'Hub')
print('sadalearninghub '*2)
#==========================================================
'''String slicing syntax : 
	str[start:end]'''
str = 'sadalearninghub'
print('First four characters in str : ', str[0:3])
print('First four characters in str : ', str[:3])
print('Last four characters in str : ', str[10:])
print('from left start from first and right start from first char : ', str[1:-1])
#=========================================================
'''String comparison : You can use ( > , < , <= , <= , == , !=  ) to compare two strings. Python compares string lexicographically i.e using ASCII value of the characters.'''
print('sada' == 'sada')
print('sadalearninghub' != 'sadalearningHub')
print('sada' < 'Sada')
print('Sasa' > 'Sada')
print('sada' <= 'Sada')
print('Sasa' >= 'Sada')

'''Iterating string using for loop'''
for char in str:
	print(char)

#=========================================================

'''Built-in String Functions : 
	ord() - function returns the ASCII code of the character.'''
print('ASCII code of the b : ', ord('b'))

'''	chr() - function returns character represented by a ASCII num'''
print('ASCII Character of the number 97 is : ', chr(97))

'''	len() 	returns length of the string'''
print('Length of the String str is : ', len(str))

'''	max() 	returns character having highest ASCII value'''
print('highest ASCII value from String str is : ', max(str))

'''	min() 	returns character having lowest ASCII value'''
print('lowest ASCII value from String str is : ', min(str))

'''	in  and not in  operators : check existence of string in another string.'''
print('check sada is there in str or not : ', 'sada' in str)


'''Testing strings
	isalnum() : Returns True if string is alphanumeric'''
print('Check string is alphanumeric : ', str.isalnum())
'''	isalpha() : Returns True if string contains only alphabets'''
print('check string contains only alphabets : ', str.isalpha())
'''	isdigit() : Returns True if string contains only digits'''
print('Check string contains only digits : ', str.isdigit())
'''	isidentifier() : Return True is string is valid identifier'''
#print('Check string is valid identifier : ', str.isidentifier()
'''	islower() : Returns True if string is in lowercase'''
print('Check string is in lowercase : ',str.islower())
'''	isupper() : Returns True if string is in uppercase'''
print('Check string is in uppercase : ', str.isupper())
'''	isspace() : Returns True if string contains only whitespace'''
print('Check string contains only whitespace : ', str.isspace())


'''Searching for Substrings
	endswith(s1: str): bool : Returns True if strings ends with substring s1'''
print('Check strings ends with substring or not : ',str.endswith("Hub"))

'''	startswith(s1: str): bool : Returns True if strings starts with substring s1'''
print('Check strings starts with substring or not : ', str.startswith("sada"))

'''	count(substring): int : Returns number of occurrences of substring the string'''
print('check number of occurrences of substring the string : ', str.count("sada"))

'''	find(s1): int : Returns lowest index from where s1 starts in the string, if string not found returns -1'''
print('Check lowest index from where s1 starts in the string : ', str.find("learning"))

'''	rfind(s1): int : Returns highest index from where s1 starts in the string, if string not found returns -1'''
print('Check highest index from where s1 starts in the string : ', str.rfind("sada"))


'''Converting Strings : 
	capitalize(): str - Returns a copy of this string with only the first character capitalized.'''
print('a copy of this string with only the first character capitalized : ',str.capitalize())

'''	lower(): str - Return string by converting every character to lowercase'''
print('string by converting every character to lowercase : ', str.lower())

'''	upper(): str - Return string by converting every character to uppercase'''
print('string by converting every character to uppercase  : ', str.upper())

'''	title(): str - This function return string by capitalizing first letter of every word in the string'''
print('string by capitalizing first letter of every word in the string : ', str.title())

'''	swapcase(): str - Return a string in which the lowercase letter is converted to uppercase and uppercase to lowercase'''
print('string in which the lowercase letter is converted to uppercase and uppercase to lowercase : ', str.swapcase())

'''	replace(old, new): str - This function returns new string by replacing the occurrence of old string with new string'''
print('New string by replacing the occurrence of old string with new string : ', str.replace("sada", "SADA"))

'''
ord() - function returns the ASCII code of the character.
chr() - function returns character represented by a ASCII number.
len() - returns length of the string
max() - returns character having highest ASCII value
min() - returns character having lowest ASCII value

Testing strings : 
isalnum() - Returns True if string is alphanumeric
isalpha() - Returns True if string contains only alphabets
isdigit() - Returns True if string contains only digits
isidentifier() - Return True is string is valid identifier
islower() - Returns True if string is in lowercase
isupper() - Returns True if string is in uppercase
isspace() - Returns True if string contains only whitespace

Searching for Substrings:
endswith(s1: str): bool - Returns True if strings ends with substring s1
startswith(s1: str): bool - Returns True if strings starts with substring s1
count(substring): int - Returns number of occurrences of substring the string
find(s1): int - Returns lowest index from where s1 starts in the string, if string not found returns -1
rfind(s1): int - Returns highest index from where s1 starts in the string, if string not found returns -1

Converting Strings:
capitalize(): str - Returns a copy of this string with only the first character capitalized.
lower(): str - Return string by converting every character to lowercase
upper(): str - Return string by converting every character to uppercase
title(): str - This function return string by capitalizing first letter of every word in the string
swapcase(): str - Return a string in which the lowercase letter is converted to uppercase and uppercase to lowercase
replace(old, new): str This function returns new string by replacing the occurrence of old string with new string'''
