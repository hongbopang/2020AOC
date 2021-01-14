# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:35:22 2020

@author: hongb
"""
import copy
import time    
        
f = open("input.txt", "r")


    

def evaluateWeird(argStr):
    ans = -1
    opcode = 0
    number_storer = 0
    ptr = 0
    subStringFlag = False
    subStringCount = 0
    subStringStart = 0
    
    while ptr < len(argStr):
        char = argStr[ptr]          
        if subStringFlag:        
            if char == '(':
                subStringCount += 1
            elif char == ')':            
                 
                 subStringCount -= 1                 
                 if subStringCount == 0:                    
                    subString = argStr[subStringStart:ptr]                    
                    newString = str(evaluateWeird(subString))   
                    argStr = argStr[:subStringStart-1] + newString + argStr[ptr+1:]                    
                    subStringFlag = False                    
                    ptr = subStringStart - 2             
                    
              
            
        elif subStringFlag == False:              
            if char == '(':    
                subStringFlag = True
                subStringStart = ptr+1
                subStringCount = 1
            if char == ' ':
                if ans == -1:
                    ans = number_storer   
                    
                else:
                    if opcode == 1:
                        ans += number_storer
                    if opcode == 2:
                        ans *= number_storer                  
                        
                number_storer = 0           
                    
                    
            elif char.isnumeric():
                number_storer *= 10
                number_storer += int(char)    
                
                
            elif char == "+":
                opcode = 1
                ptr += 1
    
            elif char == "*":
                opcode = 2
                ptr += 1
        ptr += 1
        
      
    if ans == -1:
        return number_storer
    if opcode == 1:
        ans += number_storer
    if opcode == 2:
        ans *= number_storer     
    
    
    
    return ans
                
           
             

            
        
ans = 0
for line in f:    
    line = line.strip()
    ans += evaluateWeird(line)
    
print(ans)
    




        
    




