# -*- coding: utf-8 -*-

import os.path
import time
import datetime
from grab import Grab


g = Grab()
links = []


def page_check():
    if g.response.code == 400:
        print ('%s > CODE 400: Bad Request!' % datetime.datetime.now())
        exit()
    elif g.response.code == 401:
        print ('%s > CODE 401: Unauthorized!' % datetime.datetime.now())
        exit()
    elif g.response.code == 403:
        print ('%s > CODE 403: Forbidden!' % datetime.datetime.now())
        exit()
    elif g.response.code == 404:
        print ('%s > CODE 404: Not Found!' % datetime.datetime.now())
        exit()
    elif g.response.code == 408:
        print ('%s > CODE 408: Request Timeout!' % datetime.datetime.now())
        exit()
    elif g.response.code == 500:
        print ('%s > CODE 500: Internal Server Error!' % datetime.datetime.now())
        exit()
    elif g.response.code == 502:
        print ('%s > CODE 502: Bad Gateway!' % datetime.datetime.now())
        exit()
    elif g.response.code == 503:
        print ('%s > CODE 503: Service Unavailable!' % datetime.datetime.now())
        exit()
    elif g.response.code == 504:
        print ('%s > CODE 504: Gateway Timeout!' % datetime.datetime.now())
        exit()


def url_correcting(self, url):
    if url.find('/') != -1:
        url = self.site + url
    else:
        url = self.link + url
    if ' ' in url:
        url = url.replace(' ', '%20')
    return url


class Parser:
    def __init__(self):
        self.link = ''
        self.file_format = ''
        self.keyword = ''
        self.logging = False
        self.debug = False
        self.question = False
        self.site = ''
        self.text = []
        self.strings = []

    def var_check(self):
        if len(self.link) == 0:
            print ('%s > WARNING: Site link is not defined in "parser" module!' % datetime.datetime.now())
            exit()
        elif len(self.file_format) == 0:
            print ('%s > WARNING: File format is not defined in "parser" module!' % datetime.datetime.now())
            exit()
        else:
            if self.link[len(self.link)-1] != '/':
                self.link += '/'
            self.site = self.link.replace('http://', '')
            self.site = 'http://' + self.site[:self.site.find('/')]

    def parse(self, link, file_format, keyword, debug, logging):
        self.link = link
        self.file_format = file_format
        self.keyword = keyword
        self.debug = debug
        self.logging = logging
        self.var_check()
        g.go(self.link)
        if g.response.code != 200:
            self.link = link + '?'
            g.go(self.link)
        if self.debug:
            print ('%s > Writing debug file...' % datetime.datetime.now())
            g.setup(log_file='debug.txt')
            with open('debug.txt', 'w') as f:
                f.write(g.response.body)
                f.close()
        page_check()
        print ('%s > Parsing...' % datetime.datetime.now())
        num = 1
        for elem in g.doc.select('//a'):
            url = elem.attr('href')
            txt = elem.text()
            if self.file_format in url:
                # url = self.url_correcting(url)
                url = g.make_url_absolute(url)
                if links.count(url) == 0:
                    links.append(url)
                    self.text.append(txt)
                    self.strings.append(chr(9) + str(num) + '. ' + txt + ': ' + str(links[len(links) - 1]))
                    num += 1
            elif self.keyword in txt:
                # url = self.url_correcting(url)
                url = g.make_url_absolute(url)
                if links.count(url) == 0:
                    links.append(url)
                    self.text.append(txt)
                    self.strings.append(chr(9) + str(num) + '. ' + txt + ': ' + str(links[len(links) - 1]))
                    num += 1
        self.log_out()

    def gen_urls(self, patch):
        if len(patch) == 0:
            print ('%s > WARNING: Patch is not defined in "parser" module!' % datetime.datetime.now())
            exit()
        elif len(links) == 0:
            print ('%s > WARNING: Links list is empty in "parser" module!' % datetime.datetime.now())
            exit()
        else:
            print ('%s > Generating *.urls-file...' % datetime.datetime.now())
            f = open(patch, 'w')
            for i in range(len(links)):
                f.write(links[i].encode("utf-8") + '\n')
            f.close()
        
    def gen_html(self, patch):
        if len(patch) == 0:
            print ('%s > WARNING: Patch is not defined in "parser" module!' % datetime.datetime.now())
            exit()
        elif len(links) == 0:
            print ('%s > WARNING: Links list is empty in "parser" module!' % datetime.datetime.now())
            exit()
        else:
            dtime = datetime.datetime.now()
            print ('%s > Generating *.html-file...' % datetime.datetime.now())
            f = open(patch, 'w')
            f.write('<html>\n')
            f.write(str(chr(9) + '<head>\n'))
            f.write(str(2*chr(9) + '<meta charset="utf-8"> \n'))
            f.write(str(2*chr(9) + '<title>Parser test results</title>\n'))
            f.write(str(chr(9) + '</head>\n'))
            f.write(str(chr(9) + '<body>\n'))
            f.write(str(2*chr(9) + '<h3>Parser test results:</h3>\n'))
            f.write(str(2*chr(9) + '<b>Datetime Stamp:</b> %s, %s:%s:%s<br>\n') % (dtime.date(), dtime.hour, dtime.minute, dtime.second))
            f.write(str(2*chr(9) + '<b>URL:</b>' + ' ' + '<a href="' + self.link + '">' + self.link + '</a><br>\n'))
            f.write(str(2*chr(9) + '<b>Page title:</b>' + ' ' + g.doc.select('//title').text() + '<br>\n'))
            f.write(str(2*chr(9) + '<b>File file_format:</b>' + ' ' + '*' + self.file_format + '<br><br>\n'))
            f.write(str(2*chr(9) + '<b>Site links:</b><br>\n'))
            f.write(str(2*chr(9) + '<ol type="1">\n'))
            for i in range(len(links)):
                f.write(str(3*chr(9) + '<li>' + self.text[i].encode("utf-8") + ': <a href="' + links[i].encode("utf-8") + '">' + links[i].encode("utf-8") + '</a></li>\n'))
            f.write(str(2*chr(9) + '</ol><br>\n'))
            f.write(str(2*chr(9) + '<b>Total results count:</b> %s\n' % len(self.strings)))
            f.write(str(chr(9) + '</body>\n'))
            f.write(str('</html>\n'))
            f.close()

    def log_out(self):
        if self.logging:
            print ('\nResults:')
            for i in range(len(self.strings)):
                print (self.strings[i])
            print ('\nTotal results count: %s\n' % len(self.strings))


class Load_URLS:
    def load_urls(self, patch, rewrite):
        if len(patch) == 0:
            print ('%s > WARNING: Patch to *.urls file is not defined in "load_urls" module!' % datetime.datetime.now())
            exit()
        elif not os.path.isfile(patch):
            print ('%s > WARNING: File "%s" is not exist!' % (datetime.datetime.now(), patch))
            exit()
        else:
            print ('%s > Loading URLs from "%s" file...' % (datetime.datetime.now(), patch))
            if rewrite:
                del links[:]
            with open(patch, 'r') as f:
                for line in f:
                    tmp = line
                    if '\n' in tmp:
                        tmp = tmp.replace('\n', '')
                    links.append(tmp)
                f.close()


class Get:
    def __init__(self):
        self.link = ''
        self.file_format = ''
        self.save_path = ''
        self.filename = ''
        self.name = ''
        self.extension = ''
        self.patch = ''
        self.ext_check = False

    def var_check_single(self):
        if len(self.link) == 0:
            print ('%s > WARNING: Link on file is not defined in "get" module!' % datetime.datetime.now())
            exit()
        elif len(self.file_format) == 0:
            print ('%s > WARNING: File format is not defined in "get" module!' % datetime.datetime.now())
            exit()

    def var_check_list(self):
        if len(self.file_format) == 0:
            print ('%s > WARNING: File format is not defined in "get" module!' % datetime.datetime.now())
            exit()
        elif len(links) == 0:
            print ('%s > WARNING: Empty links list in "get" module!' % datetime.datetime.now())
            exit()

    def filename_extract(self, link):
        if link.rfind(self.file_format) != -1:
            self.filename = link[(link.rfind('/') + 1):]
            self.filename = self.filename.replace('%20', ' ')
            self.filename = self.filename.replace('%26', ' ')
            self.name = self.filename[:self.filename.rfind('.')]
            self.extension = self.filename[self.filename.rfind('.'):]

    def format_check(self):
        if self.ext_check:
            if self.extension != self.file_format:
                print('%s > WARNING: File on selected link is not *%s file!' % (datetime.datetime.now(), self.file_format))
                exit()

    def get_file(self):
        print ('%s > Downloading file, link: %s...' % (datetime.datetime.now(), self.link))
        g.go(self.link)
        print ('%s > Extracting file name...' % datetime.datetime.now())
        self.filename_extract(g.response.url)
        # print ('link: ' + g.response.url + ', file: ' + self.filename)
        self.format_check()
        if len(self.save_path) <= 1:
            self.patch = self.save_path + self.filename
        else:
            self.patch = self.save_path + '/' + self.filename
        print ('%s > Saving "%s" file on disc...' % (datetime.datetime.now(), self.filename))
        with open('%s' % self.patch, 'wb') as f:
            f.write(g.response.body)
            f.close()
        print ('%s > File "%s" has been saved successfully.' % (datetime.datetime.now(), self.filename))

    def get_single(self, link, file_format, save_patch, ext_check):
        self.link = link
        self.file_format = file_format
        self.save_path = save_patch
        self.ext_check = ext_check
        self.var_check_single()
        self.get_file()

    def get_list(self, file_format, save_patch, ext_check):
        self.file_format = file_format
        self.save_path = save_patch
        self.ext_check = ext_check
        self.var_check_list()
        for i in range(len(links)):
            self.link = links[i]
            self.get_file()
