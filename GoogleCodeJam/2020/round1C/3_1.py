

from collections import Counter
import numpy as np 

def checkdouble(a_list):
    l = len(a_list)
    for i in range(l):
        for j in range(l):
            if a_list[i] == 2* a_list[j]:
                return True
    return False

def solve():
    N,D = map(int,input().split())
    a_list = list(map(int,input().split()))
    max_a = max(a_list)

    a_cnt = Counter(a_list) # {size: num}
    
    # a_cumsum = np.cumsum(a_cnt.values)
    # a_cumsum_dict = {}
    # for i ,k in enumerate(a_cnt.keys()):
    #     a_cumsum_dict[k] = a_cumsum[i]
    a_cnt_sorted = sorted(a_cnt.items(), key=lambda x:x[1],reverse=True)

    freq_a = a_cnt_sorted[0]
    if freq_a[1]>=D:
        return 0

    elif D==2:
        return 1
    
    # D=3
    k=0
    while a_cnt_sorted[k][1]==2:
        if max_a != a_cnt_sorted[k][0]:
            return 1
        k+= 1
        if k ==len(a_cnt_sorted):
            break
    if checkdouble(a_list):
        return 1
    else:
        return 2

               



T = int(input())

for n in range(1,T+1):
    ans = solve()
    print('Case #'+str(n)+': '+str(ans))

