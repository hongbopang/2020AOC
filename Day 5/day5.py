# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:35:22 2020

@author: hongb
"""



f = open("input.txt", "r")
candidates =[]

for line in f:
    data = line[:-1]
    ID = 0
    for indexer in range(7):
        ID *= 2
        if data[indexer] == 'B':
            ID += 1

    for indexer in range(7,10):
        ID *=2
        if data[indexer] == "R":
            ID += 1

    if ID > ans:
        ans = ID
        new_entries = ans - len(candidates) + 2
        candidates += [0] * new_entries
    if ID:

        candidates[ID-1] += 1
    candidates[ID+1] += 1
    candidates[ID] -= 1

print(ans)
print(candidates.index(2))
