# -*- coding:utf-8 -*-
# Edited by bighead 19-2-3

from myThread import MyThread
from time import sleep, ctime

def fib(x):
    sleep(0.005)
    if x < 2: return 1
    return (fib(x-2) + fib(x-1))

def fac(x):
    sleep(0.1)
    if x < 2: return 1
    return (x * fac(x-1))

def sum(x):
    sleep(0.1)
    if x < 2: return 1
    return (x + sum(x-1))

funcs = [fib, fac, sum]
n = 12

def main():
    nfuncs = range(len(funcs))

    print("*** SINGLE THREAD")
    for i in nfuncs:
        print("starting {} at: {}".format(funcs[i].__name__, ctime()))
        print(funcs[i](n))
        print("{} finished at: {}".format(funcs[i].__name__, ctime()))

    print("\n*** MULTIPLY THREAD")
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (n, ), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
        print(threads[i].getResult())

    print("ALL DONE")

if __name__ == "__main__":
    main()
