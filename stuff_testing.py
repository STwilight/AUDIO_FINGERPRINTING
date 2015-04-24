# -*- coding: utf-8 -*-

lines = 1
r = 0  # Чтобы было, чем заполнять
mas = []

'''
mas.append([])
mas[0].append('№')
mas.append([])
mas[1].append('Ссылка')
mas.append([])
mas[2].append('Фактическая ссылка')
mas.append([])
mas[3].append('Имя файла')
mas.append([])
mas[4].append('Совпадение')
'''

for i in range(5):
    mas.append([])
    for j in range(lines):
        mas[i].append('str ' + str(r))
        r += 1
    print mas

'''
for i in range(5):
    for j in range(lines):
        print('tr = ' + str(j+1) + ', td = ' + str(i+1) + ': '+ mas[i][j])
'''

# print (mas[1][0])


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