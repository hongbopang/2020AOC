# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:35:22 2020

@author: hongb
"""



f = open("input.txt", "r")
trees = []



for lines in f:
    trees.append(lines[:-1])

def tree_finder(xmod,ymod):
    ans = 0
    width = len(trees[0])
    height = len(trees)
    x = 0
    y = 0
    while y < height:
        if trees[y][x] == '#':
            ans += 1
        x = (x+xmod) % width

        y+=ymod
    return ans

print(tree_finder(3,1))
print(tree_finder(1,1)*tree_finder(3,1)*tree_finder(5,1)*tree_finder(7,1)*tree_finder(1,2))
