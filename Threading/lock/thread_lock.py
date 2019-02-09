# -*- coding:utf-8 -*-
# Edited by bighead 19-2-4

from atexit import register
from random import randrange
from threading import Thread, currentThread
from time import sleep, ctime

class CleanOutputSet(set):
    def __str__(self):
        return ", ".join(x for x in self)

loops = (randrange(2, 5) for x in xrange(randrange(3, 7)))
remaining = CleanOutputSet()

def loop(nsec):
    myname = currentThread().name
    remaining.add(myname)
    print("[{}] Started {}".format(ctime(), myname))
    sleep(nsec)
    remaining.remove(myname)
    print("[{}] Completed {} ({} secs)".format(ctime(), myname, nsec))
    print("    (remaining {})".format(remaining or 'NONE'))

def _main():
    for pause in loops:
        print(pause)
        Thread(target=loop, args=(pause,)).start()

@register
def _atexit():
    print("all done at: {}".format(ctime()))

if __name__ == "__main__":
    _main()
