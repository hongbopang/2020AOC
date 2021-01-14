# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:35:22 2020

@author: hongb
"""

import copy
f = open("input.txt", "r")

def gameStateToString(p1,p2):
    p1String = ""
    p2String = ""
    for p1Card in p1.deck:
        p1String += str(p1Card) + " "
    for p2Card in p2.deck:
        p2String += str(p2Card) + " "
    return p1String + "| " + p2String
    

def combat(p1,p2):
    while len(p1.deck) and len(p2.deck):
        p1Card = p1.deck.pop(0)
        p2Card = p2.deck.pop(0)
    
        if p1Card > p2Card:
            p1.deck.append(p1Card)
            p1.deck.append(p2Card)
        else:
            p2.deck.append(p2Card)
            p2.deck.append(p1Card)
        
    if (len(p1.deck) > len(p2.deck)):
        winner = p1
    else:
        winner = p2
    score = 0     
    
    for counter in range(len(winner.deck)):
        multiplier = len(winner.deck) - counter
        score += multiplier * winner.deck[counter]
    return(winner.number,score)
    

def reccombat(p1,p2):
    memory = dict()
    
    while len(p1.deck) and len(p2.deck):
        
        gameState = gameStateToString(p1,p2)
        if gameState in memory:
            return 1, 0
        memory[gameState] = 1
        
        
        p1Card = p1.deck.pop(0)
        p2Card = p2.deck.pop(0)
        
        if p1Card <= len(p1.deck) and p2Card <= len(p2.deck):
            p1tmp = copy.deepcopy(p1)
            p1tmp.deck = p1.deck[0:p1Card]

            p2tmp = copy.deepcopy(p2)
            p2tmp.deck = p2.deck[0:p2Card]
            winner, score = reccombat(p1tmp,p2tmp)
        elif p1Card > p2Card:
            winner = 1
        else:
            winner = 2
    
        if winner == 1:
            p1.deck.append(p1Card)
            p1.deck.append(p2Card)
        else:
            p2.deck.append(p2Card)
            p2.deck.append(p1Card)

    if (len(p1.deck) > len(p2.deck)):
        final_winner = p1
    else:
        final_winner = p2
    score = 0     
    
    for counter in range(len(final_winner.deck)):
        multiplier = len(final_winner.deck) - counter
        score += multiplier * final_winner.deck[counter]
    return(final_winner.number,score)


class player:
    def __init__(self,number):
        self.number = number
tmpPlayer = 0   
players = dict()
for line in f:
    line = line.strip()
    if line[0:6] == "Player":
        tmpPlayer = player(int(line[7]))
        cards = []
    elif tmpPlayer:
        if line:
            cards.append(int(line))
        else:
            tmpPlayer.deck = cards
            players[tmpPlayer.number] = tmpPlayer
            
tmpPlayer.deck = cards
players[tmpPlayer.number] = tmpPlayer   

p1 = players[1] 
recp1 = copy.deepcopy(p1)
p2 = players[2] 
recp2 = copy.deepcopy(p2)

"""    
winner,score = (combat(p1,p2))

print(winner,score)
"""
winner,score = (reccombat(recp1,recp2))

print(winner,score)
       
    

    




        
    




