# -*- coding: utf-8 -*-

import datetime
import URLSpider

get = URLSpider.Get()
parser = URLSpider.Parser()
load = URLSpider.Load_URLS()
recognize = URLSpider.Recognizer()

# parser.parse('http://www.ex.ua/17091228', '.mp3', 'mp3', False, True)   # http://symrak.fuckoff.ch/test # http://www.ex.ua/17091228
# parser.gen_urls('links.urls')
# parser.gen_html('web/report.html')
# load.load_urls('links.urls', True)
# get.get_single('http://www.ex.ua/get/34147440', '.mp3', 'mp3_downloads', False)  # http://symrak.fuckoff.ch/test/audio1.mp3
# get.get_list('.mp3', 'mp3_downloads', False)
# recognize.recognize('mp3_samples', 'mp3_downloads', '.mp3')