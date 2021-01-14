# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:35:22 2020

@author: hongb
"""
import copy
        
f = open("input.txt", "r")

mem = dict()
mem2 = dict()

part1 = 0
part2 = 1

class addr_store:
    def __init__(self,value):
        self.binary = [0 for _ in range(36)]
        counter = 0
        
        while value != 0:
            
            digit = value % 2
            value //= 2
            self.binary[counter] = digit
            counter += 1
    
    def write_value(self,value,mem,mask):
        addrs = []
        for char_index in range(len(mask.mask)):
            maskchar = mask.mask[char_index]
            if maskchar == "1":
                self.binary[char_index] = int(maskchar)
        
        addrs.append(self.return_value())
        for char_index in range(len(mask.mask)):
            maskchar = mask.mask[char_index]
            if maskchar == "X":   
                tmp = []
                modifier = int(2 ** char_index)
                if self.binary[char_index] == 1:
                    modifier *= -1
                for number in addrs:
                    tmp.append(number + modifier)
                addrs += tmp
        
        for addr in addrs:
            if addr not in mem:
                mem[addr] = 0
            mem[addr] =  value
        
                
            
            
            
    def return_value(self):
        ans = 0
        for i in range(len(self.binary)):
            ans += self.binary[i] * (2 ** i)
        return int(ans)
        
    
    
class binary_store:
    def __init__(self,value):
        self.binary = [0 for _ in range(36)]
        counter = 0
        
        while value != 0:
            
            digit = value % 2
            value //= 2
            self.binary[counter] = digit
            counter += 1
            
    def apply_mask(self,mask):
        for charindex in range(len(mask.mask)):
            if mask.mask[charindex].isnumeric():
                self.binary[charindex] = int(mask.mask[charindex])
            
    def return_value(self):
        ans = 0
        for i in range(len(self.binary)):
            ans += self.binary[i] * (2 ** i)
        return int(ans)

class mask:
    def __init__(self,mask):
        self.mask = mask[::-1]




for line in f:
    a = line.strip()        
    if a[0:4] == "mask":
        curr_mask = a[7:]
        tmp_mask = mask(curr_mask)
    else:
        args = a.split(" = ")
        location = args[0][:-1]
        location = int(location[4:])
        value = int(args[1])
        if part1:            
            tmp = binary_store(value)
            tmp.apply_mask(tmp_mask)
            if location not in mem:
                mem[location] = 0
            mem[location] = tmp.return_value()
        elif part2:
            tmp = addr_store(location)
            tmp.write_value(value,mem2,tmp_mask)

ans1 = 0        
for location in mem:
    ans1 += mem[location]
print(ans1)

ans2=0
for location in mem2:
    ans2 += mem2[location]
print(ans2)
        

   


    




