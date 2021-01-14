# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:35:22 2020

@author: hongb
"""
import copy
        
f = open("input.txt", "r")

lines = []

for line in f:
    a = line.strip()        
    lines.append(a)
    
time = int(lines[0])
buses = lines[1].split(",")
usable_buses = []
time_to_wait = []

bus_mod_target = {}


for bus in buses:
    if bus.isnumeric():
        usable_buses.append(int(bus))
        time_to_wait.append(int(bus) - time % int(bus))
        bus_mod_target[int(bus)] = (0-buses.index(bus)) % int(bus) #N:x
        
bus_index = time_to_wait.index(min(time_to_wait))

def find_inverse(mod_target, divisor): #C, N  
    #pesudo code taken from http://www.math.cmu.edu/~bkell/21110-2010s/extended-euclidean.html, (Kell, 2010)
    dividend = mod_target
    remainder = 1
    
    aies = [0,1] # there is no physical meaning to this, these seeded values allows iterations 0 and 1 to retain the same equation
    counter = 0
    # In each iteration, a new eqution of r = pe+qn can be formed. The iteration stops when remainder is 1
    
    while 1:   
        
        quotient = dividend//divisor            
        remainder = dividend - divisor*quotient    
        aies.append(aies[counter]-aies[counter+1]*quotient)  
        if remainder == 1:
            return (aies[-1] % mod_target)
        if remainder == 0:
            return 0 #if gcd is anything other than 1 than something has gone wrong in earlier steps
        dividend = divisor
        divisor = remainder
    
        counter += 1
        
def x0_finder(x0: int, n0: int, x1: int, n1: int):
    #pesudo code taken from https://www.geeksforgeeks.org/using-chinese-remainder-theorem-combine-modular-equations/
    A = x0*n1*find_inverse(n0,n1)+x1*n0*find_inverse(n1,n0)
    
    N = n0*n1
    x = A % N
    return x,N

count = 0

for n in bus_mod_target:
    print(n)
    if count == 0:
        N = n
        X = bus_mod_target[n]
    else:
        X, N = x0_finder(X,N,bus_mod_target[n],n)
    print(X,N)
    count += 1
        
print(X,N)
   


    




