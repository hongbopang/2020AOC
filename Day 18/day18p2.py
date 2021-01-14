# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 14:46:37 2020

@author: hongb
"""


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
    
    
    while '(' in argStr:
        
        subStringStart = argStr.index('(')
        
        count = 1
        pointer = subStringStart+1
        while pointer < len(argStr):            
        
            if argStr[pointer] == "(":
                count += 1
            elif argStr[pointer] == ")":
                count -= 1
                if count == 0 :
                    subString = argStr[subStringStart+1:pointer]

                    newString = str(evaluateWeird(subString)) 

                    argStr = argStr[:subStringStart] + newString + argStr[pointer+1:]    
                    break

                     
            pointer += 1
                    
                    
    while '+' in argStr and '*' in argStr:
        plus_firsts = argStr.split(" * ")
        tmpString = ""
        for subString in plus_firsts:
            tmpString += str(evaluateWeird(subString)) + " * "
        tmpString = tmpString[:-3]
        argStr = tmpString
                    
    if '+' not in argStr or '*' not in argStr:            
        while ptr < len(argStr):
            char = argStr[ptr]   
        
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
    a = evaluateWeird(line)

    ans+=a
print(ans)
    




        
    




