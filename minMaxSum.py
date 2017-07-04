#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))

arr.sort()

min = arr[0:4]
max = arr[len(arr)-4:len(arr)]

print(sum(min), sum(max), sep=" ")