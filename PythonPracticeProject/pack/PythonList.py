'''Creating python list : '''
l1 = ['SadaLearningHub', 'sada', 1990, 100]
l2 = [100, 200, 300, 400, 500, 600]
l3 = ['z', 'y', 'x', 'r']
#============================================
'''Accessing Values : '''
print('Value in 0 index : ', l1[0])
print('Values from 1 to 5 index : ', l1[1:5])
#============================================
'''Updating Values in List : '''
print('Befor updating the value in l1[3] : ', l1[3])
l1[3] = 'SadasivaRao'
print('After updating the value in l1[3] : ', l1[3])
#=============================================
'''Delete values from the list : '''
print('Before delete value from the List : ', l1)
del l1[3]
print('After delete value from the List : ', l1)
#=================================================
'''Basic List Operations : 
1.Find Length'''
print('Length of the list l1 : ', len(l1))
'''2.concatenation '''
print('Concatenation of two list l1 and l2: ', l1+l2)
'''3.Repetition'''
print('Repetition method in list : ', ['SadaLearningHub']*4)
'''4.Checking Membership in List'''
print('checking Membership in Lisst : ', 'sada' in l1)
'''5.Iteration '''
print('Iteration example start')
for x in l1:
    print(x)
print('Iteration example end')
#================================================
'''Indexing, Slicing and Matrixes in list : Indexing offset start at zero'''
print('second index value of list is : ', l1[2])
print('from right to second index value of the list is : ', l1[-2])
print('Slicing of the list from 1 to 3 is : ', l1[1:3])
#==================================================
'''Built-in List Functions and Methods
Functions:'''
a=[1,2,3,4]
b=[3,4,5,6]
print(a)
print(b)
print('Lenght of the list a is : ', len(a))
print('Max value from list a is : ',max(a))
print('Min value from list a is : ',min(a))

'''Methods : '''
print("Before Append: ", a)
a.append(5)
print("After Append: ", a)
print("Count Method Ex : ", a.count(5))
print("display the lowest index in list obj appears is : ", a.index(5))
print("Insert element into perticular index ex : ", a.insert(5,6))
print("Remove or return last object from the list : ", a.pop())
print("Remove or return last object from the list : ", a.pop(2))
print("After pop operation on the list is : ", a)
print("befor remove Method : ", a)
a.remove(2)
print("after remove Method: ", a)
print("Reverse of the List : ", a.reverse())
print("Before sort : ", a)
a.sort()
print("after sort : ", a)

