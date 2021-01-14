# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:35:22 2020

@author: hongb
"""

f = open('input.txt','r')

pks = []

def loop(val,subj):
    val *= subj
    val %= 20201227
    return val

def loop_finder(key,subj):
    val = 1
    loop_size = 0
    while val != key:
        val = loop(val,subj)
        loop_size += 1
    return loop_size
    


for line in f:
    line = int(line.strip())
    pks.append(line)


loops = []

for key in pks:
    loops.append(loop_finder(key,7))

loops.reverse()

ans = []
for component in range(2):
    pk = pks[component]
    loop_count = loops[component]
    val = 1
    for _ in range(loop_count):
        val = loop(val,pk)
    ans.append(val)
    
print(ans)




    
