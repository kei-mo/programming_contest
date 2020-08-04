from bisect import bisect_left
import numpy as np
N,K = map(int,input().split())
a_list = list(map(int,input().split()))
np.abs(a_list).sort()

ans = 1

for i in range(K):
    ans *= a_list[i]
    if a_list[i]>=0:
        last_p = a_list[i]
    else:
        last_n = a_list[i]

if ans <0:
    next_p = None
    next_n = None
    for i in range(K,N):
        if a_list[i] >=0:
            if next_p is None:
                next_p = a_list[i]
        else:
            if next_n is None:
                next_n = a_list[i]
        if (next_n is not None and next_p is not None):
            break
    if next_n is None:
        ans = ans/last_n * next_p
    elif next_p is None:
        ans = ans/last_n * next_n
    else:
        ans = max(ans/last_n * next_p, ans/last_n * next_n)
    
print(int(ans%1_000_000_007))


        