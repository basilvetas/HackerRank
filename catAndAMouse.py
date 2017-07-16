#!/bin/python3

import sys

def solve(x, y, z):
    
    if(abs(z-x) == abs(z-y)):
        return "Mouse C"
    elif(abs(z-x) < abs(z-y)):
        return "Cat A"
    else: 
        return "Cat B"

q = int(input().strip())
for a0 in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    print(solve(x, y, z))   