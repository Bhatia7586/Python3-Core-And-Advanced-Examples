#!/usr/bin/env python

import Cookie

import cgi

# set the cookie to expire
c=Cookie.SimpleCookie()
c['SadaLearningHub']=''
c['SadaLearningHub']['expires']='Thu, 01 Jan 1970 00:00:00 GMT'

# print the HTTP header
print c
print "Content-type: text/html\n\n"


print """
<html>
<body>
<center>
<h1>The cookie has been set to expire</h1>
</center>
</body>
</html>
"""
