# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 12:49:29 2020

@author: hongb
"""

partone = 0
parttwo = 1
f = open("input.txt", "r")
entries = []
for lines in f:
    entries.append(int(lines))    
for i in range(len(entries)):
    for j in range(len(entries)):
        if partone:
            if entries[i] + entries[j] == 2020:
                print (entries[i] * entries[j])
        elif parttwo:
            for k in range(len(entries)):
                if entries[i] + entries[j] + entries[k] == 2020:
                    print (entries[i] * entries[j] * entries[k])
                    