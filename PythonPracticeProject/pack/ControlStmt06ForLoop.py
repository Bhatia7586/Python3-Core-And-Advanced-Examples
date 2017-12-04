#!/usr/bin/python


'''Syntax of For Loop : 
for iterating_var in sequence:
   statements(s)
'''

for letter in 'SadaLearningHub':
    print ('Current Letter :', letter)

channelName = ['Sada', 'Learning',  'Hub']
for part in channelName:
    print ('Current part :', part)


scriptLanguages = ['ruby', 'python',  'unix']
for index in range(len(scriptLanguages)):
    print ('Current Scripting Language :', scriptLanguages[index])

for num in range(10,20): 
    print ("From Range", num)
