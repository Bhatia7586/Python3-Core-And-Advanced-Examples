#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 

cgitb.enable()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
f_name = form.getvalue('fname')
l_name  = form.getvalue('lname')

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Hello Word - GET/Post Method Example</title>'
print '</head>'
print '<body>'
print '<center>'
print '<h2>Hello This is Get Method Example</h2>'
print '<h2>Firstname is %s</h2>'% f_name
print '<h2>Lastname is %s</h2>'% l_name
print '</center>'
print '</body>'
print '</html>'


#GET 
#http://localhost/cgi-enabled/welcome.py?fname=sada&lname=sadalearninghub
#http://localhost/cgi-enabled/welcome.py?fname=SadaLearningHub&lname=+Youtube+Channel


#POST
#http://localhost/cgi-enabled/welcome.py
