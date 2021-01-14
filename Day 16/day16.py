# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:35:22 2020

@author: hongb
"""
        
f = open("input.txt", "r")

conditions = []
mytix = []
othertix = []

ptrs = [conditions,mytix,othertix]
ptr = 0
for line in f:
    a = line.strip()      
    if not a:
        ptr += 1
    else:
        ptrs[ptr].append(a)

con = dict()

for term in conditions:
    name, nums = term.split(": ")
    num1, num2 = nums.split(" or ")
    num1min, num1max = num1.split("-")
    num2min, num2max = num2.split("-")
    con[name] = [int(num1min),int(num1max),int(num2min),int(num2max)]

othertix.pop(0)
othernums = []

for tix in othertix:
    ticket = list(map(int,tix.split(",")))
    othernums.append(ticket)

invalids = 0
valids = []

for ticket in othernums:
    oldinvalid = invalids
    for num in ticket:
        invalids += num
        for condition in con:
            rule  = con[condition]
            if rule[0] <= num and num <= rule[1] or rule[2] <= num and num <= rule[3]:

                invalids -= num
                break
    if oldinvalid == invalids:
        valids.append(ticket)
mytix.pop(0)
myticket = list(map(int,mytix[0].split(",")))

print(myticket)
canfulfill = []

for condition in con:
    rule  = con[condition]
    tmp = []
    for arg_num in range(len(valids[0])):
        can_add = 1
        for ticket in valids:
            num = ticket[arg_num]
            if rule[0] <= num and num <= rule[1] or rule[2] <= num and num <= rule[3]:
                continue
            else:
                can_add = 0
                break
        if can_add:
            tmp.append(arg_num)
    canfulfill.append(tmp)

counter = 1
ruletoarg = dict()
used = []

while 1:
    for index in range(len(canfulfill)):
        if len(canfulfill[index]) == counter:
            for num in canfulfill[index]:
                if num not in used:
                    used.append(num)
                    ruletoarg[index] = num
    counter += 1
    if len(ruletoarg) == len(con):
        break                 
product = 1
for i in range(6):

    arg = ruletoarg[i]
    product *= myticket[arg]
    print(myticket[ruletoarg[i]])

print(product)
print(ruletoarg)




            
    





