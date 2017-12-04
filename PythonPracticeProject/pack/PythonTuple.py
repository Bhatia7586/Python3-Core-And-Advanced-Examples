
'''Creating a tuple'''
tup1 = ('SadaLearningHub', 'YoutubeChannelName', 2018, 1990);
tup2 = (90, 80, 70, 60);
tup3 = 'r', 'x', 'y', 'z';
tup4 = (40,)
#===================================================
'''Accessing Values in Tuples'''
print("zero index value from tuple : ", tup1[0])
print("1 to 5 index value from tuple : ", tup1[1:3])
#===================================================
'''Updating Tuples : 
	Tuples are immutable which means you cannot update or change the values of tuple elements. 
	updating action is not valid for the tuple'''
#tup1[0] = 100
'''create a new tuple'''
print("Tuple one is : ", tup1)
print("Tuple two is : ", tup2)
tup5 = tup1 + tup2
print("After Adding two Tuples : ", tup5)
#===================================================
'''Deleting tuples : 
	Removing individual tuple elements is not possible. 
	To explicitly remove an entire tuple, just use the del statement'''
print("Before deletion")
del tup5
#print("After deletion : ", tup5
#==================================================
'''Basic Tuple Operations : 
1.Find Length'''
print('Length of the tuple tup1 : ', len(tup1))
'''2.concatenation '''
print('Concatenation of two tuple tup1 and tup2: ', tup1+tup2)
'''3.Repetition'''
print('Repetition method in tuple : ', ('SadaLearningHub')*4)
'''4.Checking Membership in tuple'''
print('checking Membership in tuple : ', 'sada' in tup1)
'''5.Iteration '''
print('Iteration example start')
for x in tup1:
	print(x)
print('Iteration example end')
#================================================
'''Indexing, Slicing and Matrixes in tuple : Indexing offset start at zero'''
print('second index value of tuple is : ', tup1[2])
print('from right to second index value of the tuple is : ', tup1[-2])
print('Slicing of the tuple from 1 to 3 is : ', tup1[1:3])
#==================================================
'''No Enclosing Delimiters
	set of multiple objects, comma-separated, written without identifying symbols, i.e., brackets for lists, parentheses for tuples, etc., default to tuples,'''
print('xyz', -5.42e39, 20+9.6j, 'sada')
x, y = 15, 20;
print("Value of x , y : ", x,y)
#==================================================
'''Built-in List Functions
Functions:'''
a = (1,2,3,4)
b = (3,4,5,6)
print("Tuple one : ", a)
print("Tuple Two : ", b)
print('Lenght of the tuples a is : ', len(a))
print('Max value from tuples a is : ',max(a))
print('Min value from tuples a is : ',min(a))

