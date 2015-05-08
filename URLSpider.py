# -*- coding: utf-8 -*-

import json
import os
import datetime
import warnings
from grab import Grab
from dejavu import Dejavu
from dejavu.recognize import FileRecognizer


g = Grab()
links = []
real_links = []
names = []
recognized = []
params = []


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
        params.append(self.file_format)
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
            # f.write(str(2*chr(9) + '<b>Page title:</b>' + ' ' + g.doc.select('//title').text() + '<br>\n'))
            f.write(str(2*chr(9) + '<b>Page title:</b>' + ' ' + g.doc.select('//title').text().encode("utf-8") + '<br>\n'))
            f.write(str(2*chr(9) + '<b>File file_format:</b>' + ' ' + '*' + self.file_format + '<br><br>\n'))
            f.write(str(2*chr(9) + '<b>Site links:</b><br>\n'))
            f.write(str(2*chr(9) + '<ol type="1">\n'))
            for i in range(len(links)):
                # f.write(str(3*chr(9) + '<li>' + self.text[i].encode("utf-8") + ': <a href="' + links[i].encode("utf-8") + '">' + links[i].encode("utf-8") + '</a></li>\n'))
                f.write(str(3*chr(9) + '<li>' + self.text[i] + ': <a href="' + links[i] + '">' + links[i] + '</a></li>\n'))
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
    def __init__(self):
        self.patch = ''

    def var_check(self):
        if len(self.patch) == 0:
            print ('%s > WARNING: Patch to *.urls file is not defined in "load_urls" module!' % datetime.datetime.now())
            exit()
        elif not os.path.isfile(self.patch):
            print ('%s > WARNING: File "%s" is not exist!' % (datetime.datetime.now(), self.patch))
            exit()

    def load_urls(self, patch, rewrite):
        self.patch = patch
        self.var_check()
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
        self.temp_link = ''
        self.file_format = ''
        self.save_path = ''
        self.filename = ''
        self.name = ''
        self.extension = ''
        self.patch = ''
        self.ext_check = False
        self.ua_count = 0

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
            self.temp_link = link
            real_links.append(self.temp_link)
            self.filename = link[(link.rfind('/') + 1):]
            self.filename = self.filename.replace('%20', ' ')
            self.filename = self.filename.replace('%26', ' ')
            names.append(self.filename)
            self.name = self.filename[:self.filename.rfind('.')]
            self.extension = self.filename[self.filename.rfind('.'):]

    def format_check(self):
        if self.ext_check:
            if self.extension != self.file_format:
                print('%s > WARNING: File on selected link is not *%s file!' % (datetime.datetime.now(), self.file_format))
                exit()

    def get_file(self):
        g_get = Grab()
        print ('%s > Downloading file, link: %s...' % (datetime.datetime.now(), self.link))
        g_get.go(self.link)
        print ('%s > Extracting file name...' % datetime.datetime.now())
        self.filename_extract(g_get.response.url)
        # print ('link: ' + g_get.response.url + ', file: ' + self.filename)
        self.format_check()
        if len(self.save_path) <= 1:
            self.patch = self.save_path + self.filename
        else:
            self.patch = self.save_path + '/' + self.filename
        print ('%s > Saving "%s" file on disc...' % (datetime.datetime.now(), self.filename))
        with open('%s' % self.patch, 'wb') as f:
            f.write(g_get.response.body)
            f.close()
        print ('%s > File "%s" has been saved successfully.' % (datetime.datetime.now(), self.filename))
        del g_get

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


class Recognizer:
    def __init__(self):
        self.samples_patch = ''
        self.downloads_patch = ''
        self.file_format = ''

    def var_check(self):
        if len(self.samples_patch) == 0:
            print ('%s > WARNING: Samples folder is not defined in "recognizer" module!' % datetime.datetime.now())
            exit()
        elif len(self.downloads_patch) == 0:
            print ('%s > WARNING: Downloads folder is not defined in "recognizer" module!' % datetime.datetime.now())
            exit()
        elif len(self.file_format) == 0:
            print ('%s > WARNING: File format is not defined in "recognizer" module!' % datetime.datetime.now())
            exit()

    def recognize(self, samples_patch, downloads_patch, file_format):
        self.samples_patch = samples_patch
        self.downloads_patch = downloads_patch
        self.file_format = file_format
        self.var_check()
        warnings.filterwarnings('ignore')
        with open('dejavu.conf') as f:
            config = json.load(f)
        djv = Dejavu(config)

        # -= updating audio fingerprint base =-
        print ('%s > Updating fingerprints...' % datetime.datetime.now())
        djv.fingerprint_directory(self.samples_patch, [self.file_format])

        # -= recognizing downloaded files =-
        print ('%s > Recognizing files...' % datetime.datetime.now())
        for i in range(len(names)):
            file = self.downloads_patch + '/' + names[i]
            print ('%s > Now recognizing: %s' % (datetime.datetime.now(), names[i]))
            song = djv.recognize(FileRecognizer, file)
            recognized.append(song)
            print ('%s > From file we recognized: %s' % (datetime.datetime.now(), recognized[i]))
        print ('%s > Finished!' % datetime.datetime.now())


class Generate_Report:
    def __init__(self):
        self.patch = ''
        self.res_url = ''

    def var_check(self):
        if len(self.patch) == 0:
            print ('%s > WARNING: Patch for generating *.html report is not defined in "generate_report" module!' % datetime.datetime.now())
            exit()
        elif len(self.res_url) == 0:
            print ('%s > WARNING: Resource URL for generating *.html report is not defined in "generate_report" module!' % datetime.datetime.now())
            exit()

    def gen_html_report(self, patch, res_url):
        self.patch = patch
        self.res_url = res_url
        self.var_check()
        html_page = '<!DOCTYPE html>\n'
        dtime = datetime.datetime.now()
        print ('%s > Generating *.html-file...' % datetime.datetime.now())
        html_page += '<html>\n'
        html_page += chr(9) + '<head>\n'
        html_page += 2*chr(9) + '<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n'
        html_page += 2*chr(9) + '<title>Результаты анализа</title>\n'
        html_page += chr(9) + '</head>\n'
        html_page += chr(9) + '<body>\n'
        html_page += 2*chr(9) + '<h3>Результаты анализа:</h3>\n'
        html_page += 2*chr(9) + '<b>Дата и время:</b> %s, %s:%s:%s<br>\n' % (dtime.date(), dtime.hour, dtime.minute, dtime.second)
        html_page += 2*chr(9) + '<b>URL ссылка:</b> <a href="%s" target="_blank">%s</a><br>\n' % (res_url, res_url)
        html_page += 2*chr(9) + '<b>Заголовок страницы:</b> %s<br>\n' % g.doc.select('//title').text().encode("utf-8")
        html_page += 2*chr(9) + '<b>Формат файла:</b> *%s<br>\n' % params[0]
        html_page += 2*chr(9) + '<b>Совпадений:</b> %s из %s<br><br>\n' % (len(recognized), len(names))
        html_page += 2*chr(9) + '<b>Результаты:</b><br><br>\n'
        html_page += 3*chr(9) + '<table cols="5" border="1" cellspacing="0" cellpadding="5" align="left">\n'
        html_page += 4*chr(9) + '<tr>\n'
        html_page += 5*chr(9) + '<td align="center"><b>№</b></td>\n'
        html_page += 5*chr(9) + '<td align="center"><b>Ссылка</b></td>\n'
        html_page += 5*chr(9) + '<td align="center"><b>Фактическая ссылка</b></td>\n'
        html_page += 5*chr(9) + '<td align="center"><b>Имя файла</b></td>\n'
        html_page += 5*chr(9) + '<td align="center"><b>Совпадение</b></td>\n'
        html_page += 4*chr(9) + '</tr>\n'
        for i in range(len(links)):
            html_page += 4*chr(9) + '<tr>\n'
            html_page += 5*chr(9) + '<td align="center">%s</td>\n' % str(i+1)
            html_page += 5*chr(9) + '<td align="center"><a href="%s" target="_blank">link</a></td>\n' % links[i]
            html_page += 5*chr(9) + '<td align="center"><a href="%s" target="_blank">link</a></td>\n' % real_links[i]
            html_page += 5*chr(9) + '<td align="left">%s</td>\n' % names[i]
            html_page += 5*chr(9) + '<td align="left">%s</td>\n' % recognized[i]
            html_page += 4*chr(9) + '</tr>\n'
        html_page += 3*chr(9) + '</table>\n'
        html_page += chr(9) + '</body>\n'
        html_page += '</html>'
        f = open(self.patch, 'w')
        f.write(str(html_page))
        f.close()