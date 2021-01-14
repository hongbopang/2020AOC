# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:35:22 2020

@author: hongb
"""
import copy
import time    
        
f = open("input.txt", "r")

rules = dict()
strings = []
ruleOrStrings = True

for line in f:
    line = line.strip()
    if not line:
        ruleOrStrings = False
        continue
    elif ruleOrStrings:           
        
        rule = line.split(": ")
        
        ruleNum = int(rule[0])
        rules[ruleNum] = rule[1]
    else:
        strings.append(line)
    

def ruleParser(rules, index, currStrings):


    currRule = rules[index]
    newStrings = []
    if '"' in currRule:
        
        for string in currStrings:
            tmpString = string + currRule[1]
            newStrings.append(tmpString)
            
            
    elif "|" not in currRule:
        arguments = list(map(int,currRule.split(" ")))
        for i in arguments:
            
            currStrings = ruleParser(rules, i, currStrings)
            
        newStrings = currStrings
    else:
        options = currRule.split(" | ")

        for option in options:
            tmpCurr = copy.deepcopy(currStrings)
            arguments = list(map(int,option.split(" ")))
            for i in arguments:
                tmpCurr = ruleParser(rules, i, tmpCurr)
            newStrings += tmpCurr    
        
    
    return newStrings



acceptable = ruleParser(rules,0,copy.deepcopy([""]))
sums = 0
for entry in strings:
    if entry in acceptable:
        sums += 1
print(sums)


headers = ruleParser(rules,8,copy.deepcopy([""]))
tailers = ruleParser(rules,31,copy.deepcopy([""]))

sum2 = 0
    

for entry in strings:
    length = len(entry)
    if length % 8 != 0:
        continue
    else:
        args = length // 8
        if args < 3:
            continue
        group = 1
        onecounters = 0
        twocounters = 0
        flag = True
        for checker in range(args):
            
            indexer = checker * 8
            indexerend = indexer + 8

            subString = entry[indexer:indexerend]
            if subString in headers and twocounters == 0:
                onecounters += 1
            elif subString in tailers:
                twocounters += 1
            else:
                flag = False
                break
        if twocounters >= onecounters or twocounters*onecounters == 0:
            flag = False
        if flag:
            sum2 += 1
            print(twocounters,onecounters)
print(sum2)
                

                

            

    




        
    




