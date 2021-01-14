# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:35:22 2020

@author: hongb
"""


f = open("input.txt", "r")
rules = dict()

ans = 0
all_ans = 0
for line in f:
    line.strip()
    bags = line.split("contain")
    parent = bags[0][:-6]
    childs = bags[1].split(",")
    if parent not in rules:
        rules[parent] = []
    for child in childs:
        tp = child.split(" ")
        child_name = tp[2] + " " + tp[3]
        if child_name not in rules:
            rules[child_name] = []
        if parent not in rules[child_name]:
            rules[child_name].append(parent)
ans_set = set()
to_check = ["shiny gold"]
checked = set()

while to_check:
    check = to_check.pop()
    for entry in rules[check]:
        ans_set.add(entry)
        if entry not in checked:
            to_check.append(entry)
print(len(ans_set))

    

            





