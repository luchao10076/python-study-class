# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 11:33:06 2018

@author: Joey Lu
"""
def com(itr,r):
    pool=tuple(itr)
    n=len(pool)
    indice=list(range(r))
    yield tuple(pool[i] for i in indice)
    while True:
        for i in reversed(range(r)):
            if indice!=i+n-r:
                break
        else:
            return
        indice[i]+=1
        for j in range(i+1,r):
            indice[j]=indice[j-1]+1
        yield tuple(pool[i] for i in indice)
itr='abcdef'
r=2
f=com(itr,r)
print(f.send(1))



