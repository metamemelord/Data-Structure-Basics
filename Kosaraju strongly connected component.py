# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 16:11:47 2017

@author: MetaMemeLord-
"""

import sys

sys.setrecursionlimit(100010)

def allDone(k):
    for i in range(k,len(x)):
        if not done[i]:
            return i
    return -1

s = []

def dfs(node):
    if done[node]:
        return
    done[node] = True
    for i in x[node]:
        if not done[i]:
            dfs(i)
    s.append(node)

def dfs2(node,index):
    if done[node]:
        return
    done[node] = True
    for i in x_rev[node]:
        if not done[i]:
            dfs2(i,index)
    ans[index].append(node)

n,e = map(int,input().split())
x = [[] for i in range(n)]
for _ in range(e):
    v1,v2 = map(int,input().split())
    x[v1].append(v2)
done = [False] * n
k = 0
while k!=-1:
    dfs(k)
    k = allDone(k)
x_rev = [[] for _ in range(n)]
for i in range(len(x)):
    for j in x[i]:
        x_rev[j].append(i)
done = [False] * n
ans = []
index = 0
while len(s) != 0:
    k = s.pop()
    if not done[k]:
        ans.append([])
        dfs2(k,index)
        index += 1
    else:
        continue
print(list(sorted(_) for _ in sorted(ans)))

'''
Test case:
11 13
0 1
1 2
2 0
1 3
3 4
4 5
5 3
6 5
6 7
7 8
8 9
9 6
9 10
'''
