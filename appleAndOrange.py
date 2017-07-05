#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

a_house = 0
o_house = 0

for i in range(m):
    a_pos = a + apple[i]
    if(a_pos >= s and a_pos <= t):
        a_house += 1
        
for i in range(n):
    o_pos = b + orange[i]
    if(o_pos >= s and o_pos <= t):
        o_house += 1        

print("\n".join(map(str,[a_house, o_house])))