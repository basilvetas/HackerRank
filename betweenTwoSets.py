#!/bin/python3

import sys

def getTotalX(a, b):
    # Complete this function   
    a.sort()
    b.sort()
    
    x_cand = []    
    
    for x in range(1, b[0] + 1):
        if(b[0] % x == 0):
            x_cand.append(x)
    
    if(len(x_cand) == 0):
        return 0

    not_fact = []
    
    if(len(b) > 1):
        for i in range(len(x_cand)):
            for j in range(1, len(b)):
                if(b[j] % x_cand[i] != 0):  
                    not_fact.append(x_cand[i])
                    break

    x_cand = list(set(x_cand) - set(not_fact))                    
    not_x = []
    
    for k in range(len(x_cand)):
        for l in range(len(a)):
            if(x_cand[k] % a[l] != 0):
                not_x.append(x_cand[k])
                break

    return len(set(x_cand) - set(not_x))
            
n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
total = getTotalX(a, b)
print(total)