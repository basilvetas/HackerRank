#!/bin/python3

import sys

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

ct = []
for i in range(n):
    ct.append(a.count(i+1))

indices = [i for i, val_i in enumerate(ct) if val_i == max(ct)]

total = 0
for i in indices:
    val = max(ct[i] + ct[i+1], ct[i] + ct[i-1])
    if(val > total):
        total = val
print(total)