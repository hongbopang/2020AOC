# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 15:29:58 2020

@author: hongb


"""

import numpy as np
def monster_finder(maxGrid):
    dragonCount = 0
    for row in range(totalLength-3+1):
        for col in range(totalLength-20+1):
            dragonHead = [row,col]
            dragonFlag = True
            for dragonMod in modifiers:
                if maxGrid[row+dragonMod[0]][col+dragonMod[1]] != '#':
                    dragonFlag = False
                    break
            if dragonFlag:
                dragonCount += 1
    return dragonCount
class image:
    def __init__(self,number,text):
        self.number = number
        self.text = text        
        self.edges = [0,0,0,0]  
        self.oppEdges = [0,0,0,0]
        self.friends = 0
        
    def determineEdges(self):
        self.text = np.array(self.text)
        self.edges[0] = ''.join(self.text[0].astype(str))
        bot = self.text[-1]
        self.edges[2] = ''.join(np.flip(bot).astype(str))
        self.edges[1] = ''.join(self.text[:,-1].astype(str))
        left = self.text[:,0]
        self.edges[3] =''.join(np.flip(left).astype(str)) 
        
        
    def rotate(self,n):
        for _ in range(n):
            self.text = np.rot90(self.text)
        self.edges = self.edges[n:] + self.edges[:n]
        self.oppEdges = self.oppEdges[n:] + self.oppEdges[:n]
        
    def flip(self,edge):
        if edge%2 == 0: #top or bot
            self.text=np.fliplr(self.text)
            self.oppEdges[1],self.oppEdges[3] = self.oppEdges[3],self.oppEdges[1]
        else: #top or bot
            self.text=np.flipud(self.text)    
            self.oppEdges[2],self.oppEdges[0] = self.oppEdges[0],self.oppEdges[2]

        self.determineEdges()
        
            
            
            
    def find_edges(self):
        self.determineEdges()
        for edgeIndex in range(len(self.edges)):
            edge = self.edges[edgeIndex]

            if edge in listeners:
                otherNum,otherIndex = listeners[edge]
                self.oppEdges[edgeIndex] = otherNum #im connected at this edge to this piece
                pictures[otherNum].oppEdges[otherIndex] = self.number
                self.friends += 1
                pictures[otherNum].friends += 1
            elif edge[::-1] in listeners:
                otherNum,otherIndex = listeners[edge[::-1]]
                self.oppEdges[edgeIndex] = otherNum #im connected at this edge to this piece
                pictures[otherNum].oppEdges[otherIndex] = self.number
                self.friends += 1
                pictures[otherNum].friends += 1
                
            else:
                listeners[edge] = [self.number,edgeIndex]
           
f = open("input.txt", "r")
pictures = dict()
text_holder = []
tmp = ""
listeners = dict()

for line in f:
    line = line.strip()
    if not line:
        tmp.find_edges()
        pictures[tmp.number] = tmp
        tmp = []
    elif not tmp:
        number = int(line[5:9])
        tmp = image(number,[])
    else:
        tmp.text.append(list(map(str,line)))
        
gridLength = int(len(pictures) ** 0.5)      
grid = np.zeros((gridLength,gridLength))  

for picture in pictures:
    if pictures[picture].friends == 2:
        firstCorner = picture
        break
    
while pictures[firstCorner].oppEdges[1] * pictures[firstCorner].oppEdges[2] == 0:
    pictures[firstCorner].rotate(1)

grid[0][0] = firstCorner

curr = firstCorner
front = firstCorner

for indexer in range(1,gridLength):
    curr = pictures[curr]
    rightIndex = curr.oppEdges[1]
    right = pictures[rightIndex]
    edgeToMatch = curr.edges[1]
    
    if edgeToMatch in right.edges:
        right.flip(1)
    edgeToMatch = edgeToMatch[::-1]
    
    rotational_correction = right.edges.index(edgeToMatch)
    rotate = (rotational_correction - 3) % 4
    right.rotate(rotate)
    
    grid[0][indexer] = right.number

    curr = right.number
    
for rowdexer in range(1,gridLength):    
    front = pictures[front]
    
    botIndex = front.oppEdges[2]
    bot = pictures[botIndex]
    edgeToMatch = front.edges[2]
    
    if edgeToMatch in bot.edges:
        bot.flip(2)

    edgeToMatch = edgeToMatch[::-1]
    rotate = bot.edges.index(edgeToMatch)
    
    bot.rotate(rotate)
    grid[rowdexer][0] = bot.number
    front = bot.number
    curr = pictures[front]
    
    for indexer in range(1,gridLength):

        rightIndex = curr.oppEdges[1]

        right = pictures[rightIndex]
        edgeToMatch = curr.edges[1]
        
        if edgeToMatch in right.edges:
            right.flip(1)
        edgeToMatch = edgeToMatch[::-1]
        
        rotational_correction = right.edges.index(edgeToMatch)
        rotate = (rotational_correction - 3) % 4
        right.rotate(rotate)
        
        grid[rowdexer][indexer] = right.number
    
        curr = right
    
lengthOfOneUnit = len(edgeToMatch)

totalLength = gridLength*(lengthOfOneUnit -2)



maxGrid = np.empty((totalLength,totalLength),dtype=str)
hashes = 0
for outerRow in range(gridLength):
    for outerCol in range(gridLength):
        text = pictures[grid[outerRow][outerCol]].text
        for innerRow in range(1,lengthOfOneUnit-1):
            for innerCol in range(1,lengthOfOneUnit-1):
                rowArg = outerRow*8 + innerRow - 1
                colArg = outerCol*8 + innerCol - 1

                symbol = text[innerRow,innerCol]
                if symbol == '#':
                    hashes += 1
                maxGrid[rowArg][colArg] = symbol
        
modifiers = [[1,0],[2,1],[2,4],[1,5],[1,6],[2,7],[2,10],[1,11],[1,12],[2,13],[2,16],[1,17],[0,18],[1,18],[1,19]]

ans = 0
rotates = 0
flipped = 0
while ans == 0:
    ans = monster_finder(maxGrid)
    print(ans)
    if rotates < 3:
        rotates += 1
        maxGrid = np.rot90(maxGrid)        
    elif rotates == 3:
        if flipped == 0:
            maxGrid = np.fliplr(maxGrid)  
            rotates = 0
            flipped == 1
print(rotates,flipped)
print(hashes - len(modifiers) * ans)
            
        
    



