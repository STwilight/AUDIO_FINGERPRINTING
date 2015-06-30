# -*- coding: utf-8 -*-

import URLSpider

get = URLSpider.Get()
parser = URLSpider.Parser()
load = URLSpider.Load_URLS()
recognize = URLSpider.Recognizer()
report = URLSpider.Generate_Report()
screenshot = URLSpider.Screenshot()

# url = 'http://symrak.fuckoff.ch/test'
url = 'http://www.ex.ua/48711923'

# parser.parse(url, '.mp3', 'mp3', False, True)
# parser.gen_urls('links.urls')
# parser.gen_html('web/report.html')
# load.load_urls('links.urls', True)
# get.get_single('http://www.ex.ua/get/34147440', '.mp3', 'mp3_downloads', False)
# get.get_list('.mp3', 'mp3_downloads', False)
# recognize.recognize('mp3_samples', 'mp3_downloads', '.mp3')
# report.gen_html_report('web/report.html', url)

screenshot.get_screenshot('/home/newtest/AUDIO_FINGERPRINTING/scr', url)
