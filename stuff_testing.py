# -*- coding: utf-8 -*-

a = 3
b = 5
r = 0  # Чтобы было, чем заполнять
mas = []
for i in range(a):
    mas.append([])
    for j in range(b):
        mas[i].append(r)
        r += 1

print(mas[1][1])

"""
import datetime

patch = 'web/test_report.html'

html_page = '<!DOCTYPE html>\n'

dtime = datetime.datetime.now()
print ('%s > Generating *.html-file...' % datetime.datetime.now())
f = open(patch, 'w')
html_page += '<html>\n'
html_page += chr(9) + '<head>\n'
html_page += 2*chr(9) + '<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n'
html_page += 2*chr(9) + '<title>Результаты анализа</title>\n'
html_page += chr(9) + '</head>\n'
html_page += chr(9) + '<body>\n'
html_page += 2*chr(9) + '<h3>Результаты анализа:</h3>\n'
html_page += 2*chr(9) + '<b>Дата и время:</b> %s, %s:%s:%s<br>\n' % (dtime.date(), dtime.hour, dtime.minute, dtime.second)
html_page += 2*chr(9) + '<b>URL ссылка:</b> <a href="' + 'url' + '" target="_blank">'+ 'url' + '</a><br>\n'
html_page += 2*chr(9) + '<b>Заголовок страницы:</b> %s<br>\n' % 'title'
html_page += 2*chr(9) + '<b>Формат файла:</b> *%s<br>\n' % 'format'
html_page += 2*chr(9) + '<b>Совпадений:</b> %s из %s<br><br>\n' % (0, 0)
html_page += 2*chr(9) + '<b>Результаты:</b><br><br>\n'
html_page += 3*chr(9) + '<table cols="5" border="1" cellspacing="0" cellpadding="5" align="left">\n'
html_page += 4*chr(9) + '<tr>\n'
html_page += 5*chr(9) + '<td align="center"><b>№</b></td>\n'
html_page += 5*chr(9) + '<td align="center"><b>Ссылка</b></td>\n'
html_page += 5*chr(9) + '<td align="center"><b>Фактическая ссылка</b></td>\n'
html_page += 5*chr(9) + '<td align="center"><b>Имя файла</b></td>\n'
html_page += 5*chr(9) + '<td align="center"><b>Совпадение</b></td>\n'
html_page += 4*chr(9) + '</tr>\n'
for i in range(9):
    html_page += 4*chr(9) + '<tr>\n'
    html_page += 5*chr(9) + '<td align="center">%s.</td>\n' % str(i+1)
    html_page += 5*chr(9) + '<td align="center"><a href="%s" target="_blank">link</a></td>\n' % 'url'
    html_page += 5*chr(9) + '<td align="center"><a href="%s" target="_blank">link</a></td>\n' % 'url'
    html_page += 5*chr(9) + '<td align="center">%s</td>\n' % 'filename'
    html_page += 5*chr(9) + '<td align="center">%s</td>\n' % 'filename'
    html_page += 4*chr(9) + '</tr>\n'
html_page += 3*chr(9) + '</table>\n'
html_page += chr(9) + '</body>\n'
html_page += '</html>'

print (str(html_page))

f = open(patch, 'w')
f.write(str(html_page))
f.close()
"""

"""
# user-agent randomizer

from random import randint

patch = 'user-agent.list'
i = 0
f = open(patch, 'r')
for line in f:
    i += 1
f.close()
line_number = randint(0, i-1)
f = open(patch, 'r')
tmp = f.readlines()[line_number]
f.close()
if '\n' in tmp:
    tmp = tmp.replace('\n', '')
elif '\r' in tmp:
    tmp = tmp.replace('\r', '')
print(tmp)
"""