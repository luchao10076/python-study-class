# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 12:42:42 2018

@author: Joey Lu
"""
n=input().split(' ')
m=list(map(lambda x:int(x),input().split(' ')))
for i in range(int(n[1])):
    l=list(map(lambda x:int(x),input().split(' ')))
    if l[0]==2:
        l1=m[l[1]-1:l[2]]
        l2=[[]]
        for j in l1:
            l2.extend([[j]+x for x in l2])
        for k in range(1,len(l2)):
            if sum(l2[k])%(l[2]-l[1]+1)==0:
                print('YES')
                break
        else:
            print('NO')

