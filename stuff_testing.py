# -*- coding: utf-8 -*-

import json
import warnings
from dejavu import Dejavu
from dejavu.recognize import FileRecognizer

warnings.filterwarnings('ignore')
with open('dejavu.conf') as f:
    config = json.load(f)
djv = Dejavu(config)

song = djv.recognize(FileRecognizer, 'mp3_downloads/At Vance - Flight Of The Bumblebee.mp3')

print (song['song_name'])

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