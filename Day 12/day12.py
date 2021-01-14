# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:35:22 2020

@author: hongb
"""
import copy
        
f = open("input.txt", "r")




# direction also in [x,y]
# 0 is y axis (row), 1 is x axis (y)

direction_matrix = [[1,0],[0,1],[-1,0],[0,-1]] # NESW

class ship:
    def __init__(self, direction, location = [0,0]):
        self.location = location;
        self.direction = direction;
        
    def command(self,order):
        opcode = order[0]
        order = int(order[1:])
        
        if opcode == "F":
            if direction_matrix[self.direction] == [1,0]:
                opcode = "N"
            if direction_matrix[self.direction] == [-1,0]:
                opcode = "S"
            if direction_matrix[self.direction] == [0,1]:
                opcode = "E"
            if direction_matrix[self.direction] == [0,-1]:
                opcode = "W"
                
        if opcode == 'N':
            self.location[0] += order
        if opcode == 'S':
            self.location[0] -= order
        if opcode == 'E':
            self.location[1] += order
        if opcode == 'W':
            self.location[1] -= order
        if opcode == 'R':
            order = order % 360
            order /= 90
            self.direction = int((self.direction + order) % 4)
        if opcode == 'L':
            order = order % 360
            order /= 90
            self.direction = int((self.direction - order) % 4)
            
ship = ship(1)            
for line in f:
    line.strip()        
    ship.command(line)   
   
ans = 0
for a in ship.location:
    
    ans += abs(a)

    
print(ans)



