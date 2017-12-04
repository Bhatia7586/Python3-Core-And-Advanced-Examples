intglovar = 10
strglovar = 'sadalearninghub'

def fun():
	intlocalvar = 20
	strlocalvar = 'youtube channel'
	print ("local variables : ")
#'''it will return all the names that can be accessed locally from that function. The locals() returns dictionary'''
	print(locals())
fun()
print ("===================================================")
print ("Global variables :")
'''it will return all the names that can be accessed globally from that function. The globals() returns dictionary'''
print (globals())
