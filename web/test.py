#!/usr/bin/python
# -*- coding: UTF-8 -*-

import subprocess

url = 'http://google.com'
patch = '/home/newtest/AUDIO_FINGERPRINTING/web/'
file = 'ololo.png'
# cmd = 'gnome-web-photo %s %s' % (url, patch+file)
cmd = 'python pywebshot.py -f %s %s' % (file, url)

status = subprocess.call(cmd, shell=True)
# status = subprocess.call(['gnome-web-photo', 'http://google.com', 'ololo.png'], shell=True)
# status = subprocess.check_output(cmd, shell=True)

print 'Content-type: text/html'
print
print 'status: %s' % status

'''
try:
    status = subprocess.check_call(cmd)
except Exception, e:
    print e
'''