#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cgi
form = cgi.FieldStorage()
url = form.getfirst('url', 'none')
print 'Content-type: text/html'
print
print '<html><head>'
print '<title>Python Script</title>'
print '</head><body>'
print '<b>URL:</b> <a href=%s target="_blank">%s</a>' % (url, url)
print '</body></html>'