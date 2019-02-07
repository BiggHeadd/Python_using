# -*- coding: utf-8 -*-
# Edited by bighead 19-2-2

import thread
from time import sleep, ctime

def loop0():
    print("Start loop0 at: {}".format(ctime()))
    sleep(4)
    print("loop0 done at: {}".format(ctime()))

def loop1():
    print("start loop1 at: {}".format(ctime()))
    sleep(2)
    print("loop1 done at: {}".format(ctime()))

def main():
    print("starting at: {}".format(ctime()))
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    sleep(6)
    print("all done at: {}".format(ctime()))

if __name__ == "__main__":
    main()
