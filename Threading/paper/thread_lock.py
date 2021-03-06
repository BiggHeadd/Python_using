# -*- coding:utf-8 -*-
# Edited by bighead 19-2-2

import thread
from time import sleep, ctime

loops = [4, 2]

def loop(nloop, nsec, lock):
    print("start loop {}, at: {}".format(nloop, ctime()))
    sleep(nsec)
    print("loop {} done at {}".format(nloop, ctime()))
    lock.release()

def main():
    print("starting at: {}".format(ctime()))
    locks=[]
    nloops = range(len(loops))

    for i in nloops:
        lock = thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        while locks[i].locked(): pass

    print("all done at: {}".format(ctime()))


if __name__ == "__main__":
    main()
