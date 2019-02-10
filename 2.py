# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 11:01:25 2018

@author: Joey Lu
"""
n=int(input())
for i in range(n):
    m=int(input())
    l=[]
    for i in range(1,m+1):
        l.append(i)
    count=0
    while len(l)>1:
        l1=l[:]
        for j in range(len(l1)):
            count+=1
            if count%2==0:
                l.remove(l1[j])
    print(l[0])