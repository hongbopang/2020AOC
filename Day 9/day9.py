# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:35:22 2020

@author: hongb
"""
f = open("input.txt", "r")

numbers = []

for line in f:
    numbers.append(int(line.strip()))
    
possibles = []
for i in range(25):
    for j in range(25):
        if i != j:
            possibles.append(numbers[i]+numbers[j])

for indexer in range(25,len(numbers)):
    if numbers[indexer] not in possibles:
        print(numbers[indexer])
        target = numbers[indexer]
        break
    possibles = possibles[25:]
    for i in range(1,26):
        possibles.append(numbers[indexer]+numbers[indexer-i])
        
    
for i in range(len(numbers)):

    checker = 0
    pos = 0
    num_set = []
    while checker < target:
        
        num_set.append(numbers[i+pos])
        checker += numbers[i+pos]
        if checker == target and len(num_set) > 1:
            print(min(num_set)+max(num_set))
        pos += 1


    

            





