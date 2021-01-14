# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:35:22 2020

@author: hongb
"""
import copy
import time    
import numpy as np 
 
f = open("input.txt", "r")

menu = dict()
foods = dict()

for line in f:
    
    line=line.strip()
    ingredients, allergens = line.split(" (contains ")
    ingredients = ingredients.split(" ")
    
    for food in ingredients:
        if food not in foods:
            foods[food] = 0
        foods[food] += 1
    allergens = allergens[:-1]
    if ',' in allergens:
        allergens = allergens.split(", ")
    else:
        allergens = [allergens]

    for allergy in allergens:
        if allergy not in menu:
            menu[allergy] = []
            for food in ingredients:
                menu[allergy].append(food)
        else:
            previous = menu[allergy]     
            toRemove = []         
            for prevIngredients in previous:

                if prevIngredients not in ingredients:
                    toRemove.append(prevIngredients)
            for ingredient in toRemove:
                menu[allergy].remove(ingredient)



allergicStuff = set()
for allergy in menu:
    for food in menu[allergy]:
        allergicStuff.add(food)
count = 0        
for food in foods:
    if food not in allergicStuff:
        count += foods[food]

print(count)

ansMenu = dict()


while menu:
    changeFlag = False
    for allergen in menu:
        if len(menu[allergen]) == 1:
            ansMenu[allergen] = menu[allergen][0]
            idenitifedFood = menu[allergen][0]
            del menu[allergen]
            break
    for allergen in menu:
        if idenitifedFood in menu[allergen]:
            menu[allergen].remove(idenitifedFood)

            
names = []
for name in ansMenu:
    names.append(name)    

names.sort()
ansString = ""
for name in names:
    ansString += ansMenu[name] + ","

print(ansString)











                

            

    




        
    




