# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:35:22 2020

@author: hongb
"""
import copy

def print_dict(zyx,z):
    
    for y in zyx[z]:
        for x in zyx[z][y]:
            if zyx[z][y][x] == 1:
                print(z,y,x)
                
def get_sum(zyx):
    count = 0
    for z in zyx:
        for y in zyx[z]:
            for x in zyx[z][y]:
                count += zyx[z][y][x]
    return count

def add_dict(dictionary,z,y,x,val):
    
    if z not in dictionary:
        dictionary[z] = dict()
    if y not in dictionary[z]:
        dictionary[z][y] = dict()

    dictionary[z][y][x] = val
    
def count_neighbours(zyx,z,y,x):
    count = 0
    for zmod in [-1,0,1]:
        if z+zmod in zyx:            
            for ymod in [-1,0,1]:
                if y+ymod in zyx[z+zmod]:
                    for xmod in [-1,0,1]:
                        if x+xmod in zyx[z+zmod][y+ymod]:                   
                            if zmod or ymod or xmod:
                                count += zyx[z+zmod][y+ymod][x+xmod]
    return count

def check_state(zyx,z,y,x):
    
    if z not in zyx:
        return 0
    if y not in zyx[z]:
        return 0
    if x not in zyx[z][y]:
        return 0

    return zyx[z][y][x]

                
        
f = open("input.txt", "r")

zyx = dict()
ycounter = 0



for line in f:
    line = line.strip()
    for xcounter in range(len(line)):
        if line[xcounter] == "#":

            add_dict(zyx,0,ycounter,xcounter,1)

    ycounter += 1


for _ in range(6):

    newZyx = dict() 

    z_max = max(zyx)
    z_min = min(zyx)
    y_max = max(zyx[z_max])
    y_min = min(zyx[z_min])
    x_max = max(zyx[z_max][y_max])
    x_min = min(zyx[z_min][y_min])
    for z in zyx:
        if max(zyx[z]) > y_max:
            y_max = max(zyx[z])
        if min(zyx[z]) < y_min:
            y_min = min(zyx[z])
        for y in zyx[z]:
            if max(zyx[z][y]) > x_max:
                x_max = max(zyx[z][y])
            if min(zyx[z][y]) < x_min:
                x_min =min(zyx[z][y])
    z_max += 1
    y_max += 1
    x_max += 1

    z_min -= 1
    y_min -= 1
    x_min -= 1



    for z in range(z_min,z_max+1):        
        for y in range(y_min,y_max+1):
            for x in range(y_min,y_max+1):
                state = check_state(zyx, z, y, x)  
                if state == 1 and z == -1 and _ == 0:
                    print(z,y,x)

                neighbours = count_neighbours(zyx,z,y,x)
                if state == 0 and neighbours == 3:
                    add_dict(newZyx,z,y,x,1)

                elif state == 1 and (neighbours == 2 or neighbours == 3):
                    
                    add_dict(newZyx,z,y,x,1)

                else:
                    add_dict(newZyx,z,y,x,0)
                    
    zyx = copy.deepcopy(newZyx)  
    
    

print_dict(zyx,-1)
print(get_sum(zyx))            

        
    




        
    




