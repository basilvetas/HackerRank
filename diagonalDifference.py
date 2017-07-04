#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

prim = []
sec = []

for i in range(n):
    for j in range(n):
        if i == j:
            prim.append(a[i][j])
        if i == (n - j - 1):
            sec.append(a[i][j])

print(abs(sum(prim) - sum(sec)))