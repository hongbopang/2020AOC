# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:35:22 2020

@author: hongb
"""
#inputTxt = '389125467'
inputTxt = '167248359' #actual input
cups = list(map(int,inputTxt))
manyCups = list(map(int,inputTxt))


def shift_left(cups,n): 
    if n>0:
        return  cups[n:] + cups[:n]        
    else:
        return cups[n:] + cups[:len(cups)+n]   
        
def next_index(ptr,n,length):
    return (ptr+n)%length

def move(ptr,cups):
    length = len(cups)
    currCup = cups[ptr]
    
    pickup = []
    pickPtr = next_index(ptr,1,len(cups))
    
    for _ in range(3):
        pickPtr = next_index(pickPtr,0,len(cups))
        pickup.append(cups.pop(pickPtr))
        
        
    label = next_index(currCup,-1,length)
    if label == 0:
        label = length
    while label in pickup:
        label = next_index(label,-1,length)
        if label == 0:
            label = length

    labelLoc = cups.index(label)
    newCups = cups[0:labelLoc+1] + pickup + cups[labelLoc+1:]
    
    offset = newCups.index(currCup)

    if offset != ptr:

        newCups = shift_left(newCups, offset-ptr)

    # the pos of the currCup cannot change
    return next_index(ptr,1,len(newCups)),newCups
    

ptr, cups = move(0,cups)

done = 1
stepsToDo = 100
while done < stepsToDo:    
    ptr, cups = move(ptr,cups)    
    done += 1
start = cups.index(1)

ansString = ""
for _ in range(len(cups)):
    ansString += str(cups[start])
    start=next_index(start, 1, len(cups))

print("P1 ans: \n")
print(ansString[1:])

#part 2, refactored to linked list

def print_List(ptr,items): #checker function, not needed for solution
    curr = items[ptr]
    ansStr = ""
    while 1:
        ansStr += str(curr.val)
        curr = curr.next
        if curr.val == ptr:
            print(ansStr)
            break
        
def move_linked(ptr,items):
    currCup = items[ptr]
    pickUp = []
    values = [] # values of picked up cups 
    tmp = currCup
    for _ in range(3):
        pickUp.append(tmp.next)
        values.append(tmp.next.val)
        tmp = tmp.next

    currCup.next = tmp.next
    tmp.next.prev = currCup
    
    label = ptr-1
    if label == 0:
        label = len(items)
    while label in values:
        label -= 1
        if label == 0:
            label = len(items) # 0 checker can't be at the end in since there are multiple elements in the picked up pile
            
    destination = items[label]
    
    pickupHead = pickUp[0]
    pickupTail = pickUp[-1]
    
    destination.next.prev = pickupTail
    pickupTail.next = destination.next
    destination.next = pickupHead
    pickupHead.prev = destination
    
    ptr = items[ptr].next.val
    return ptr,items
totalCups = 1000000
totalMoves = 10000000

class linked_element:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

        
items = dict()
head = manyCups[0]
curr = head

items[head] = linked_element(head) #put element in dict to find element with specific val quickly

for indexer in range(1,len(manyCups)): # insert given cups
    tmp = linked_element(manyCups[indexer])
    tmp.prev = items[curr]
    items[curr].next = tmp    
    items[manyCups[indexer]] = tmp
    curr = manyCups[indexer]
   
newNumber = len(manyCups)+1

while newNumber <= totalCups: # insert non-given cups
    tmp = linked_element(newNumber)
    tmp.prev = items[curr]
    items[curr].next = tmp 
    items[newNumber] = tmp
    curr = newNumber
    newNumber += 1

items[curr].next = items[head]
items[head].prev = items[curr]

p,items = move_linked(head,items)
done = 1
while done < totalMoves:

    p,items = move_linked(p,items)
    done += 1


print(items[1].next.val,items[1].next.next.val)
print("P2 ans: \n")
print(items[1].next.val*items[1].next.next.val)