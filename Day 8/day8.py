# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:35:22 2020

@author: hongb
"""

import copy
f = open("input.txt", "r")

instructions = []

for line in f:
    line.strip()

    argument = line[:3]
    sign = line[4]
    value = int(line[5:])
    if sign == "-":
        value *= -1
    instructions.append((argument,value))

def check(lineToChange,flag):
    tmp = copy.deepcopy(instructions)
    if flag:
        if tmp[lineToChange][0] == "nop":
            tmp[lineToChange] = ("jmp",tmp[lineToChange][1])
        if tmp[lineToChange][0] == "jmp":
            tmp[lineToChange] = ("nop",tmp[lineToChange][1])
    visited = set()
    indexer = 0
    acc = 0
    ans = True
    while 1:
        if indexer == len(instructions):
            return acc,True
        ins = tmp[indexer]
        if indexer in visited:
            ans = False
            break
        visited.add(indexer)
        if ins[0] == "acc":
            acc += ins[1]
            indexer += 1
        elif ins[0] == "jmp":
            indexer += ins[1]
        else:
            indexer += 1
    return acc,ans
a,b = check(0,False)
print(b)
for lineindexer in range(len(instructions)):
    x,y = check(lineindexer,True)
    if y:
        print(x)
