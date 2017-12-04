import re

s = "My number is 7569127522"

match  = re.search(r'\d{10}',s)

print("Matched string is :",match.group())

s = "This is my sadalearninghub@gmail.com"

match = re.search(r'[\w.-]+@[\w.-]+',s)
if match:
    print("Matched string Email is :",match.group())
else:
    print("Mtch is not found")
    

#Group captureing
s = "This is my sadalearninghub@gmail.com"

match = re.search(r'([\w.-]+)@([\w.-]+)',s)
if match:
    print("Matched string Email is :",match.group())
    print("Matched string username is :",match.group(1))
    print("Matched string hostname is :",match.group(2))
else:
    print("Mtch is not found")
    
    
#Checking all mtches
s = "My number is 7569127522 no 1234567890"
match  = re.findall(r'\d{10}',s)
if match:
    print("Matched string Mobile number is :",match)
else:
    print("Mtch is not found")


s = "My phone number is 12345-67890 and 76691-27522"
match  = re.findall(r'(\d{5})-(\d{5})',s)
if match:
    print("Matched string Mobile number is :",match)
    for i in match:
        print()
        print(i)
        print("First group is : ",i[0])
        print("First group is : ",i[1])
else:
    print("Mtch is not found")


#optional flages
s = "python in sadalearninghub"
match = re.match(r'^py',s)
if match:
    print("matched string is :",match)