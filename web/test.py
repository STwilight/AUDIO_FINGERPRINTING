#!/usr/bin/python
# -*- coding: UTF-8 -*-

import subprocess

url = 'http://google.com'
patch = '/home/newtest/AUDIO_FINGERPRINTING/web/scr/'
file = 'ololo.png'


### TEST BLOCK ###

print 'Content-type: text/html\n'

cmd = 'touch %s' % (patch + 'test.txt')
try:
    status = subprocess.check_call(cmd, shell=True)
    print '<b>status</b> <i>"%s"</i> command: %s<br>' % (cmd, status)
except Exception, e:
    print '<b>exception msg</b>: %s<br>' % e

cmd = 'echo "Test string in test file" >%s' % (patch + 'test.txt')
try:
    status = subprocess.check_call(cmd, shell=True)
    print '<b>status</b> <i>"%s"</i> command: %s<br>' % (cmd, status)
except Exception, e:
    print '<b>exception msg</b>: %s<br>' % e

### TEST BLOCK ###

cmd = '/usr/bin/gnome-web-photo %s %s' % (url, patch+file)
try:
    status = subprocess.check_call(cmd, shell=True)
    print '<b>status</b> <i>"%s"</i> command: %s<br>' % (cmd, status)
except Exception, e:
    print '<b>exception msg</b>: %s<br>' % e