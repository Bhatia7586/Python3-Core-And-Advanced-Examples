#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 

cgitb.enable()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
username = form.getvalue('usr')
password  = form.getvalue('pwd')
status = ""

if username =='sada' and password == 'sada':
	status = 'success'
else:
	status = 'Failed'

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>CGI Get Example</title>"
print "</head>"
print "<body>"
print "<center>"
print "<h2><u>Login Page Details</u></h2>"
print "<h2>User Name : %s</h2>" % username
print "<h2>Login %s</h2>" % status
print "</center>"
print "</body>"
print "</html>"
