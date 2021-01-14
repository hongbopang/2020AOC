# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 13:14:23 2020

@author: hongb
"""


# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:35:22 2020

@author: hongb
"""
import copy
        
f = open("input.txt", "r")


def flip(delta):
    ans = [0,0]
    ans[0] = 0-delta[1]
    ans[1] = delta[0]
    return ans

# direction also in [x,y]
# 0 is y axis (row), 1 is x axis (y)

direction_matrix = [[1,0],[0,1],[-1,0],[0,-1]] # NESW

class ship:
    def __init__(self, direction, location = [0,0]):
        self.location = location;
        self.direction = direction;
        
    def command(self,opcode,order,waypoint):
        
        rowdel = waypoint.location[0] - self.location[0]
        coldel = waypoint.location[1] - self.location[1]

        for _ in range(order):
            waypoint.location[0] += rowdel
            waypoint.location[1] += coldel
            self.location[0] += rowdel
            self.location[1] += coldel

class waypoint:
    def __init__(self, direction, location = [0,0]):
        self.location = location;
        self.direction = direction;
        
                
    def command(self,opcode,order,ship):
        
        if opcode == 'N':
            self.location[0] += order
        elif opcode == 'S':
            self.location[0] -= order
        elif opcode == 'E':
            self.location[1] += order
        elif opcode == 'W':
            self.location[1] -= order      
        
        rowdel = ship.location[0] - self.location[0]
        coldel = ship.location[1] - self.location[1]
        
        if opcode == 'L':
            print(order)
            order = order % 360
            order /= -90
            order %= 4
            print(order)
        if opcode == 'R':
            order = order % 360
            order /= 90
        temp = [rowdel,coldel]
        if opcode == 'L' or opcode == 'R':
            for _ in range(int(order)):
                temp = flip(temp)
            self.location[0] = ship.location[0] - temp[0]
            self.location[1] = ship.location[1] - temp[1]

            
ship = ship(1)     
waypoint = waypoint(1,[1,10])       
for line in f:
    order = line.strip()   
    opcode = order[0]
    order = int(order[1:])     
    if opcode == 'F':
        ship.command(opcode,order,waypoint)
    else:
        waypoint.command(opcode,order,ship)
    #print(ship.location,waypoint.location)
   
ans = 0
for a in ship.location:

    ans += abs(a)

    
print(ans)



