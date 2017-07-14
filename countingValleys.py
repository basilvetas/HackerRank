import sys

def solve(steps):
    pos = 0
    in_val = False
    valleys = 0
    
    for i in steps:
        if(i is "U"):
            if(pos == -1):
                in_val = False
                valleys += 1
            pos += 1
        if(i is "D"):            
            if(pos >= 0):
                in_val = True
            pos -= 1
    return valleys

n = int(input().strip())
steps = list(input().strip())
result = solve(steps)
print(result)