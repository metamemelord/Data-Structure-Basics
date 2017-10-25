# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 23:38:57 2017
@author: MetaMemeLord-

This is the solution to problem in tutorial of Segment Trees on Hackerearth.
Link: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/tutorial/
"""

x = []

def getParent(node):
    global size
    return node//2 + size

def getLeftChild(node):
    global size
    return 2*(node - size)

def getRightChild(node):
    global size
    return 2*(node - size) + 1

def getMin(n,m):
    global size
    try:
        assert (n>=0 and n<size), print(end='')
        assert (m>=0 and m<size), print(end='')
    except AssertionError:
        print('Out of range!',end= ' ')
        return float('inf')
    if n==m:
        return x[n]
    else:
        minimum = float('inf')
        while n<=m:
            if n%2 == 1:
                minimum = min(minimum,x[n])
                n = getParent(n+1)
            else:
                minimum = min(minimum,x[n])
                n = getParent(n)
            if m%2 == 1:
                minimum = min(minimum,x[m])
                m = getParent(m)
            else:
                minimum = min(minimum,x[m])
                m = getParent(m-1)
        return minimum

def update(pos,val):
    global size
    x[pos] = val
    while pos < len(x)-1:
        x[getParent(pos)] = min(x[getLeftChild(getParent(pos))],x[getRightChild(getParent(pos))])
        pos = getParent(pos)

def _init():
    global size
    k = 0
    while k<len(x)-1:
        x.append(x[k] if x[k]<x[k+1] else x[k+1])
        k += 2
n,q = map(int,input().split())
x = [int(i) for i in input().split()]
size = len(x)
_init()
for _ in range(q):
    q = input().split()
    if q[0] == 'q':
        print(getMin(int(q[1]),int(q[2])))
    else:
        update(int(q[1]),int(q[2]))

'''
for _ in range(int(input())):
    n,m = map(int,input().split())
    print(getMin(n,m))

#print(list(enumerate(x)))
'''
