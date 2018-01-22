#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 

cgitb.enable()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
firstname = form.getvalue('firname')
lastname  = form.getvalue('lstname')

# Checkbox
hobbies=""
if form.getvalue('reading'):
   hobbies = "Reading "

if form.getvalue('cooking'):
   hobbies += "Cooking "

if form.getvalue('listening'):
   hobbies += "Listening "

#RadioButton
if form.getvalue('gender'):
   gender = form.getvalue('gender')
else:
   gender = "Not set"

#TextArea
if form.getvalue('textcontent'):
   text_content = form.getvalue('textcontent')
else:
   text_content = "Not entered"

#Dropdown box
if form.getvalue('dropdown'):
   edu = form.getvalue('dropdown')
else:
   edu = "Not entered"

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Register</title>"
print "</head>"
print "<body>"
print "<center>"
print "<br/><br/><br/><br/>"
print "<h2><u>Hello %s %s</u></h2>" % (firstname, lastname)
print "<br/>"
print "<b>First Name:</b>  %s" % firstname
print "<br/>"
print "<b>Last Name:</b>  %s" % lastname
print "<br/>"
print "<b>Hobiies:</b> %s" % hobbies
print "<br/>"
print "<b>Gender:</b> %s" % gender
print "<br/>"
print "<b>Comments :</b> %s" % text_content
print "<br/>"
print "<b>Education :</b> %s" % edu
print "</center>"
print "</body>"
print "</html>"
