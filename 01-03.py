# -*- coding: utf-8 -*-

'''
多项式的计算 1 + sum(x^i / i)   i=1-100
'''

def f1(x, n):
    sum = 1.0
    for i in range(1, n + 1):
        sum = sum + pow(x, i) / float(i)
    return sum

def f2(x, n):
    l = range(1, n + 1)
    l.reverse()
    p = 1.0 / l.pop(0)
    for i in l:
        p = p * x + 1.0 / i
    return p * x + 1.0

if __name__ == '__main__':
    print f1(1.1, 100)
    print f2(1.1, 100)
    from timeit import Timer
    t1 = Timer('f1(1.1, 100)', 'from __main__ import f1')
    t2 = Timer('f2(1.1, 100)', 'from __main__ import f2')
    print t1.timeit(100000)
    print t2.timeit(100000)
    print t1.repeat(3, 100000)
    print t2.repeat(3, 100000)

