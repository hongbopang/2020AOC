# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:35:22 2020

@author: hongb
"""
import copy
import time
        
f = open("input.txt", "r")

mem = {}

class num_mem:
    def __init__(self, latest):
        self.latest = latest
        self.memory = -1
                 

for line in f:
    a = line.strip()        
    numbers = list(map(int,a.split(",")))

counter = 0
spoken = []

while counter < len(numbers):
    num = numbers[counter]
    tmp = num_mem(counter)    
    mem[num] = tmp
    spoken.append(num)    
        
    counter += 1
t1 = time.time()      
while counter < 30000000:
    
    num = spoken[-1]

  
    if mem[num].memory == -1:
        spoken.append(0)
        tmp = mem[0]
        tmp.memory = tmp.latest
        tmp.latest = counter
        
    else:
        last_num_mem = mem[num]

        next_num = last_num_mem.latest - last_num_mem.memory
        spoken.append(next_num)        
        
        if next_num not in mem:
            new_num_mem = num_mem(counter)
            mem[next_num] = new_num_mem
        else:
            old_num_mem = mem[next_num]
            old_num_mem.memory = old_num_mem.latest
            old_num_mem.latest = counter
 
    
    
    
    counter += 1

t2 = time.time()  


print(spoken[-1])
       






