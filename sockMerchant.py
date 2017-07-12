#!/bin/python3

import sys

def sockMerchant(n, ar):
    # Complete this function    
    pairs = 0
    colors = set(ar)
    
    for c in colors:
        pairs += int(ar.count(c) / 2)
            
    return pairs

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)