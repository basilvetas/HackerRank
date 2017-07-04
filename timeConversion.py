#!/bin/python3

import sys

def timeConversion(s):
    
    # Complete this function
    hh = int(s[0:2])
    mmdd = s[2:len(s)-2]
    ampm = s[len(s)-2: len(s)]
    
    if(ampm == "PM" and hh < 12):
        hh += 12    
    elif(ampm == "AM"):
        hh = hh % 12

    if(hh < 10):
        hrs = "0" + str(hh)  
    else: 
        hrs = str(hh)

    return hrs + mmdd 
    
s = input().strip()
result = timeConversion(s)
print(result)