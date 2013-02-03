#!/usr/bin/python2

from HTMLParser import HTMLParser
import os

html_unescape = HTMLParser().unescape

for ofn in (f for f in os.listdir('.') if f.lower().endswith('.mp3')):
    nfn = html_unescape(ofn.decode('unicode_escape'))
    os.rename(ofn, nfn.encode('utf-8'))

    
