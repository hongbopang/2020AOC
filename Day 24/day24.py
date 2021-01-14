# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:35:22 2020

@author: hongb
"""

f = open('input.txt','r')

flipped = dict()

#e 0,2 w 0,-2, se -1,1 sw -1-1 ne 1,1 nw 1-1

def findFriend(rowcol,flipped):
    address = str(rowcol[0]) + " " + str(rowcol[1])
    if address in flipped:
        return 1, address
    return 0, address
    
def countFriendsForBlack(string,flipped):
    row,col = list(map(int,string.split(" ")))
    neighbours = []
    neighbours.append([row,col+2])
    neighbours.append([row,col-2])
    neighbours.append([row+1,col+1])
    neighbours.append([row+1,col-1])
    neighbours.append([row-1,col+1])
    neighbours.append([row-1,col-1])
    friends = 0
    formatedNeighbours = []
    for neighbour in neighbours:
        value, address = findFriend(neighbour,flipped)
        friends += value
        formatedNeighbours.append(address)
    return formatedNeighbours,friends
    
    
    
    
curr = ""
for line in f:
    line = line.strip()    
    row = col = 0
    for char in line:
        curr += char
        if curr == 'e':
            col += 2
            curr = ""
        elif curr == 'w':
            col -= 2     
            curr = ""
        elif curr == 'se':
            row -= 1
            col += 1
            curr = ""
        elif curr == 'sw':
            row -= 1
            col -= 1
            curr = ""
        elif curr == 'ne':
            row += 1
            col += 1
            curr = ""
        elif curr == 'nw':
            row += 1
            col -= 1
            curr = ""

    address = str(row) + " " + str(col)
    
    if address not in flipped:
        flipped[address] = 1
    else:
        del flipped[address]
        
        
for day in range(100):
    new = dict()
    whiteChecker = dict()
    for black in flipped:
        neighbours, friends = countFriendsForBlack(black,flipped)
        if friends == 1 or friends == 2:
            new[black] = 1
        for neighbour in neighbours: # check each neighbour of a black tile...
            if neighbour not in flipped: #excluding already black tiles...
                if neighbour not in whiteChecker:
                    whiteChecker[neighbour] = 0
                whiteChecker[neighbour] += 1
    for white in whiteChecker:
        if whiteChecker[white] == 2:
            new[white] = 1
    flipped = new
    print(day+1,len(new))

    
