#!/bin/python3

import sys

def solve(n, s, d, m):
    # Complete this function
    total = 0
    for i in range(n):
        sum = s[i]
        for j in range(i, n):
            ind = j + 1
            if(ind-i == m):
                if(sum == d):
                    total += 1
                    break
            elif(ind-i < m and ind < n):
                sum += s[ind]
            else:
                break

    return total                
            
                
            

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)