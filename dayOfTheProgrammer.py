#!/bin/python3

import sys

def solve(year):
    # Complete this function   
    feb = 28
    if(year >= 1919):
        if(year % 400 == 0):
            feb = 29
        elif(year % 4 == 0 and year % 100 != 0):
            feb = 29
    elif(year <= 1917):
        if(year % 4 == 0):
            feb = 29

    mm = "09"
    dd = 256 - (31 + feb + 31 + 30 + 31 + 30 + 31 + 31)
    if(year == 1918):
        dd = 256 - (46 + 31 + 30 + 31 + 30 + 31 + 31)
        
    dd = str(dd)
    date = dd + "." + mm + "." + str(year)
    return date
        

year = int(input().strip())
result = solve(year)
print(result)