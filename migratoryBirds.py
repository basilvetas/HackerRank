#!/bin/python3

import sys

def migratoryBirds(n, ar):
    # Complete this function
    bird_type = 0
    max_freq = 0
    
    for i in range(1, 6):
        if(ar.count(i) > max_freq):
            max_freq = ar.count(i)            
            bird_type = i
        elif(ar.count(i) == max_freq and i < bird_type):
            max_freq = ar.count(i)            
            bird_type = i

    return bird_type            

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
