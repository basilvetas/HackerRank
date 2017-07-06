#!/bin/python3

import sys

def getRecord(s):
    # Complete this function
    max = s[0]
    max_ct = 0
    min = s[0]
    min_ct = 0
    for i in range(1, len(s)):
        if(s[i] > max):
            max = s[i]
            max_ct += 1
        
        if(s[i] < min):
            min = s[i]
            min_ct += 1

    return max_ct, min_ct
    

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))