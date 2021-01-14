# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:35:22 2020

@author: hongb
"""
import copy

                
def get_sum(wzyx):
    count = 0
    for w in wzyx:
        for z in wzyx[w]:
            for y in wzyx[w][z]:
                for x in wzyx[w][z][y]:
                    count += wzyx[w][z][y][x]
    return count

def add_dict(dictionary,w,z,y,x,val):
    if w not in dictionary:
        dictionary[w] = dict()
    if z not in dictionary[w]:
        dictionary[w][z] = dict()
    if y not in dictionary[w][z]:
        dictionary[w][z][y] = dict()

    dictionary[w][z][y][x] = val
    
def count_neighbours(wzyx,w,z,y,x):
    count = 0
    for wmod in [-1,0,1]:
        if w+wmod in wzyx:
            for zmod in [-1,0,1]:
                if z+zmod in wzyx[w+wmod]:            
                    for ymod in [-1,0,1]:
                        if y+ymod in wzyx[w+wmod][z+zmod]:
                            for xmod in [-1,0,1]:
                                if x+xmod in wzyx[w+wmod][z+zmod][y+ymod]:                   
                                    if wmod or zmod or ymod or xmod:
                                        count += wzyx[w+wmod][z+zmod][y+ymod][x+xmod]
    return count

def check_state(wzyx,w,z,y,x):
    if w not in wzyx:
        return 0
    if z not in wzyx[w]:
        return 0
    if y not in wzyx[w][z]:
        return 0
    if x not in wzyx[w][z][y]:
        return 0

    return wzyx[w][z][y][x]

                
        
f = open("input.txt", "r")

wzyx = dict()
ycounter = 0



for line in f:
    line = line.strip()
    for xcounter in range(len(line)):
        if line[xcounter] == "#":

            add_dict(wzyx,0,0,ycounter,xcounter,1)

    ycounter += 1

print(wzyx)

for _ in range(6):

    newWzyx = dict() 

    w_max = max(wzyx)
    w_min = min(wzyx)
    z_max = max(wzyx[w_max])
    z_min = max(wzyx[w_min])
    
    y_max = max(wzyx[w_max][z_max])
    y_min = min(wzyx[w_max][z_min])
    x_max = max(wzyx[w_max][z_max][y_max])
    x_min = min(wzyx[w_max][z_min][y_min])
    for w in wzyx:
        if max(wzyx[w]) > z_max:
            z_max = max(wzyx[w])
        if min(wzyx[w]) < z_min:
            z_min = min(wzyx[w])
        for z in wzyx[w]:
            if max(wzyx[w][z]) > y_max:
                y_max = max(wzyx[w][z])
            if min(wzyx[w][z]) < y_min:
                y_min =min(wzyx[w][z])
            for y in wzyx[w][z]:
                if max(wzyx[w][z][y]) > x_max:
                    x_max = max(wzyx[w][z][y])
                if min(wzyx[w][z][y]) < x_min:
                    x_min =min(wzyx[w][z][y])
    w_max += 1    
    z_max += 1
    y_max += 1
    x_max += 1

    w_min -= 1
    z_min -= 1
    y_min -= 1
    x_min -= 1


    for w in range(w_min,w_max+1):
        for z in range(z_min,z_max+1):        
            for y in range(y_min,y_max+1):
                for x in range(x_min,x_max+1):
                    state = check_state(wzyx, w,z, y, x)  

                    neighbours = count_neighbours(wzyx,w,z,y,x)
                    if state == 0 and neighbours == 3:
                        add_dict(newWzyx,w,z,y,x,1)
    
                    elif state == 1 and (neighbours == 2 or neighbours == 3):
                        
                        add_dict(newWzyx,w,z,y,x,1)
    
                    else:
                        add_dict(newWzyx,w,z,y,x,0)
                    
    wzyx = copy.deepcopy(newWzyx)  
    
    


print(get_sum(wzyx))            

        
    




        
    




