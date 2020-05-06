
import numpy as np 


def solve():
    x,y,path = input().split()
    curx, cury = int(x), int(y)

    ans = np.inf
    for i, m in enumerate(list(path)):
        t = i+1
        prex = curx
        prey = cury

        if m=="S":
            curx = prex
            cury = prey - 1
        elif m=="N":
            curx = prex
            cury = prey + 1
        elif m=="E":
            curx = prex + 1
            cury = prey 
        elif m=="W":
            curx = prex - 1
            cury = prey

        cost_t = abs(curx) + abs(cury) # time need to visit (curx,cury)
        if cost_t<=t: # can visit in time t
            if ans>t:
                ans = t
    return ans 

T = int(input())

for n in range(1,T+1):
    ans = solve()
    if ans==np.inf:
        print('Case #'+str(n)+': IMPOSSIBLE')
    else:
        print('Case #'+str(n)+': '+ str(ans))


    
