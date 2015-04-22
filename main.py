# -*- coding: utf-8 -*-

# -= importing lib components =-
import URLSpider
import warnings
import datetime
import json
import os
from dejavu import Dejavu
from dejavu.recognize import FileRecognizer

# -= setting up warnings =-
warnings.filterwarnings('ignore')

print ('\n%s > Starting...' % datetime.datetime.now())
print ('%s > Loading configs and initialization...' % datetime.datetime.now())

# -= loading configs =-
with open('dejavu.cnf.SAMPLE') as f:
    config = json.load(f)

# -= creating objects =-
parser = URLSpider.Parser()
load = URLSpider.Load_URLS()
get = URLSpider.Get()
djv = Dejavu(config)

# -= execution =-
# parser.parse('http://www.ex.ua/17091228', '.mp3', 'mp3', False, True)   # http://symrak.fuckoff.ch/test
# parser.gen_urls('links.urls')
# parser.gen_html('index.html')

# load.load_urls('links.urls', True)

# get.get_single('http://www.ex.ua/get/34147440', '.mp3', 'mp3_downloads', False)  # http://symrak.fuckoff.ch/test/audio1.mp3
# get.get_list('.mp3', 'mp3_downloads', False)

'''
# -= updating audio fingerprint base =-
print ('%s > Updating fingerprints...\n' % datetime.datetime.now())
djv.fingerprint_directory('mp3_samples', ['.mp3'])

# -= recognizing downloaded files =-
print ('\n%s > Recognizing files...' % datetime.datetime.now())
downloads_dir = 'mp3_downloads'
files = os.listdir(downloads_dir)
files = filter(lambda x: x.endswith('.mp3'), files)
for i in range(len(files)):
    print ('%s > Now recognizing: %s' % (datetime.datetime.now(), files[i]))
    song = djv.recognize(FileRecognizer, downloads_dir + '/' + files[i])
    print ('%s > From file we recognized: %s' % (datetime.datetime.now(), song))
print ('%s > Finished!' % datetime.datetime.now())
'''