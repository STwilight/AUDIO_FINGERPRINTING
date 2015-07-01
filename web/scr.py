#!/usr/bin/python
# -*- coding: UTF-8 -*-

#import os
import cgi
import datetime
import subprocess

patch = '/home/newtest/AUDIO_FINGERPRINTING/web/scr'
html_escape_table = {'&': '&amp;', '"': '&quot;', "'": '&apos;', '>': '&gt;', '<': '&lt;'}
error = False


def html_escape(text):
    return "".join(html_escape_table.get(c, c) for c in text)

form = cgi.FieldStorage()
url = form.getfirst('url', 'none')
url = html_escape(url)


def request_processing(err):
    if (url.find('http://') and url.find('https://')) == -1:
        print '            <img src="images/error.png" width="64" height="64" alt="error!"><br>'
        print '            <font color="red"><b>WARNING:</b></font> Resource URL is incorrect! <a href="/drm">Re-enter</a> an address.'
        err = True
    else:
        print '            <img src="images/loading.gif" width="64" height="64" alt="loading..."><br>'
        print '            <b>Loading image from </b><a href=%s target="_blank">%s</a><b> site...</b>' % (url, url)
        err = False
    return err


def generate_savepatch(folder_patch, res_url):
    dtime = datetime.datetime.now()
    scr_site = res_url
    timestamp = '%s_%s.%s.%s' % (dtime.date(), dtime.hour, dtime.minute, dtime.second)
    if url.find('http://') != -1:
        scr_site = scr_site.replace('http://', '')
    elif url.find('https://') != -1:
        scr_site = scr_site.replace('https://', '')
    scr_site = scr_site[:scr_site.find('/')]
    savepatch = folder_patch + '/' + timestamp + '_' + scr_site + '.png'
    return savepatch


def get_screenshot(folder_patch, res_url):
    file_patch = generate_savepatch(folder_patch, res_url)
    cmd = 'gnome-web-photo %s %s' % (res_url, file_patch)
    # if "os.system(cmd)" will be used, os.system module needs to be imported
    pipe = subprocess.PIPE
    p = subprocess.Popen(cmd, shell = True)

print 'Content-type: text/html\n'
print '<!DOCTYPE HTML>'
print '<html>'
print '    <head>'
print '        <meta charset="utf-8">'
print '        <link rel="shortcut icon" href="images/favicon.ico" type="image/x-icon">'
print '        <title>Processing...</title>'
print '    </head>'
print '    <body>'
print '        <center>'
print '            <br><br><br><br><br>'
error = request_processing(error)
print '        </center>'
print '    </body>'
print '</html>'

if not error:
    get_screenshot(patch, url)