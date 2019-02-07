# -*- coding:utf-8 -*-
# Edited by bighead 19-2-3

from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib2 import urlopen as uopen
import requests

REGEX = compile("#([\d,]+) in Books ")
AMZN = "http://amazon.com/dp/"
ISBNs = {
    '0132269937': 'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals',
}

def getRanking(isbn):
    print(AMZN+isbn)
    page = requests.get(AMZN+isbn)
    data = page.text
    page.close()
    return REGEX.findall(data)[0]

def _showRanking(isbn):
    print("- %r ranking %s" % (ISBNs[isbn], getRanking(isbn)))

def main():
    print("At {} on Amazon...".format(ctime()))
    for isbn in ISBNs:
        _showRanking(isbn)
        # print(isbn)

@register
def _atexit():
    print("all done at: {}".format(ctime()))

if __name__ == "__main__":
    main()
