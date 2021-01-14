# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:35:22 2020

@author: hongb
"""
import copy

one = 0
two = 1

class cell:
    def __init__(self,row,col,state):
        self.row = row
        self.col = col
        self.state = state
        
    def find_neighbours(self):
        
        rows = [-1,0,1]
        count = 0
        if self.row == 0:
            rows.remove(-1)
        elif self.row == len(old_map) - 1:
            rows.remove(1)
        cols = [-1,0,1]
        if self.col == 0:
            cols.remove(-1)
        elif self.col == len(old_map[0]) - 1:
            cols.remove(1)
        
        for i in rows:
            for j in cols:
                if i != 0 or j != 0:
                    
                    if old_map[self.row+i][self.col+j].state == '#':   
                        count += 1
        return count
    def find_neighbours2(self):
        count = 0
        
        rows = [-1,0,1]
        cols = [-1,0,1]
        
        directions = [[i,j] for i in rows for j in cols]
        directions.remove([0,0])
        
        for lineOfSight in directions:
            r = self.row
            c = self.col
            while 1:
                r += lineOfSight[0]
                c += lineOfSight[1]
                if r < 0 or c < 0 or r == len(old_map) or c == len(old_map[0]):
                    break
                elif old_map[r][c].state == "#":
                    count += 1
                    break
                elif old_map[r][c].state == "L":
    
                    break
        

        return count
                    
    def update_map(self,new_map,flag):
        if one:
            friends = self.find_neighbours()
            toomanyfriends = 4
        else:
            friends = self.find_neighbours2()
            toomanyfriends = 5
        if self.state == 'L' and friends == 0:
            new_map[self.row][self.col] = cell(self.row,self.col,'#')
            flag = True
        elif self.state == '#' and friends >= toomanyfriends:
            new_map[self.row][self.col] = cell(self.row,self.col,'L')
            flag = True
        else:
             new_map[self.row][self.col] = cell(self.row,self.col,self.state)

        return flag
        
f = open("input.txt", "r")

map_prime = []
row = 0
for line in f:
    tmp = []
    for char_indexer in range(len(line.strip())):
        tmp.append(cell(row,char_indexer,line[char_indexer]))    
    map_prime.append(tmp)
    row+=1
    
rows = len(map_prime)
cols = len(map_prime[0])


old_map = copy.deepcopy(map_prime)
flag = True





while flag:
    flag = False
    new_map = copy.deepcopy(old_map)
    for row in range(rows):
        ts = []
        for col in range(cols):
            flag = old_map[row][col].update_map(new_map,flag)

            ts.append(new_map[row][col].state)
        

    old_map = copy.deepcopy(new_map)

        
    
ans = 0
for row in range(rows):
    for col in range(cols):
        if old_map[row][col].state == "#":
            ans += 1
print(ans)

            





