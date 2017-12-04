
'''Create Dictionary'''
emailinfo = {'sada' : 'sada@gmail.com', 
            'gopi' : 'gopi@gmail.com', 
            'venki' : 'venki@gmail.com'}
print(emailinfo)
#=============================================================

'''Retrieving, modifying and adding elements in the dictionary'''
print(emailinfo['sada'])	#Retrieving
emailinfo['sada'] = 'sda492@gmail.com'	#modifying
print('after Modifiing sada key value is : ',emailinfo['sada'])
emailinfo['ram']='ram@gmail.com' #adding elements
print('After adding New key and value into dictionary : ', emailinfo)
print('Before deletion : ', emailinfo)
del emailinfo['ram'] #deletion
print('After deletion : ', emailinfo)
#==========================================================

'''Looping items in the dictionary'''
for key in emailinfo:
  print(key, ":", emailinfo[key])
#==========================================================

'''Find the length of the dictionary'''
print(len(emailinfo))

'''in or not in operators'''
print('sada' in emailinfo)
print('ram' not in emailinfo)

'''Equality Tests in dictionary'''
d1 = {1:'x', 2:'y', 3:'z'}
d2 = {1:'x', 2:'y', 3:'z'}
print('check equality of two dictionaries : ', d1 == d2)
print('check non equality of two dictionaries : ', d1 != d2)
#==========================================================

print('email info : ', emailinfo)
'''Dictionary methods
	popitem() - Returns randomly select item from dictionary and also remove the selected item.'''
print('remove the selected item : ', emailinfo.popitem())

'''	keys() - Return keys in dictionary as tuples'''
print('keys in dictionary : ', emailinfo.keys())

'''	values() - Return values in dictionary as tuples'''
print('values in dictionary : ', emailinfo.values())

'''	get(key) - Return value of key, if key is not found it returns None, instead on throwing KeyError exception'''
print('Return value of key : ', emailinfo.get('sada'))

'''pop(key) - Remove the item from the dictionary, if key is not found KeyError will be thrown'''
print('Remove the item from the dictionary : ', emailinfo.pop('sada'))

'''	clear() - Delete everything from dictionary'''
print('Delete everything from dictionary : ', emailinfo.clear())


