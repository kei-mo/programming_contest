

from collections import Counter
import numpy as np 

def checkmulitpe(a_cnt,tsize):
    l = []
    for size in a_cnt.keys():
        if size>tsize:
            if tsize%size==0:
                l.append[size]
    return l



def solve():
    N,D = map(int,input().split())
    a_list = list(map(int,input().split()))
    max_a = max(a_list)

    a_cnt = Counter(a_list) # {size: num}
    
    cnt = N
    bigger_a_dict = {}
    for i ,k in enumerate(a_cnt.keys()):
        cnt -= a_cnt[k]
        bigger_a_dict[k] = cnt
    stats = sorted(a_cnt.items(), key=lambda x:x[1],reverse=True)

    ans = D-1
    for i in range(len(stats)):
        size = stats[i][0]
        num = stats[i][1]
        bigger_num = bigger_a_dict[size]      # size より大きいサイズの枚数
        need = D-num
        cut = D-num
        multisize = checkmulitpe(a_cnt,size) # multsのものを使用していく
        for s in multisize:
            if multisize//size>=need:
                need -= multisize//size
                cut -= 1 
        if cut >= bigger_num:
            if cut<ans:
                ans = cut
    return ans 
        


T = int(input())

for n in range(1,T+1):
    ans = solve()
    print('Case #'+str(n)+': '+str(ans))

