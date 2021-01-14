# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:35:22 2020

@author: hongb
"""
import copy
import time    
import numpy as np


       
class image:
    def __init__(self,number,text):
        self.number = number
        self.text = text        
        self.edges = [0,0,0,0]  #upright(0 upright, 1 turn right, 2 turn down, 3 turn left), if reflected +4
        self.friends = 0
        self.friendEdges = [0,0,0,0]

    def find_edges(self):
        self.text = np.array(self.text)

        self.edges[0] = ''.join(self.text[0].astype(str))
        bot = self.text[-1]
        self.edges[2] = ''.join(np.flip(bot).astype(str))
        self.edges[1] = ''.join(self.text[:,-1].astype(str))
        left = self.text[:,0]
        self.edges[3] =''.join(np.flip(left).astype(str)) 

        for edgeIndex in range(len(self.edges)):
            edge = self.edges[edgeIndex]
            if edge in listeners :
                pictures[listeners[edge][0]].friends += 1                  
                self.friendEdges[edgeIndex] = listeners[edge][0] * -1              
                pictures[listeners[edge][0]].friendEdges[listeners[edge][1]] = self.number
                self.friends += 1
                
            elif edge[::-1] in listeners:
                pictures[listeners[edge[::-1]][0]].friends += 1                  
                self.friendEdges[edgeIndex] = listeners[edge[::-1]][0]           
                pictures[listeners[edge[::-1]][0]].friendEdges[listeners[edge[::-1]][1]] = self.number
                
                self.friends +=1
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




length = int(len(pictures)**0.5)
product = 1

grid = np.zeros((12,12))

firstCorner = 0


for tmp in pictures:
    print(tmp,pictures[tmp].friendEdges)
    if pictures[tmp].friends == 2:
        product *= tmp
        if not firstCorner:
            firstCorner = pictures[tmp]

print(product)       











                

            

    




        
    




