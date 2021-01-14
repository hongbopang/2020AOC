# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 13:12:20 2020

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
        if tp[1] == "no":
            child_q = 0
        else:
            child_q = int(tp[1])
        rules[parent].append((child_name,child_q))




def bags_in_me(bag_tag):
    if bag_tag not in rules:
        return 0
    bags = 0
    for baggies in rules[bag_tag]:
        bags += baggies[1] * (1+ bags_in_me(baggies[0]))
    return bags
print(bags_in_me("shiny gold"))

