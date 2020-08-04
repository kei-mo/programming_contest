import numpy as np 
import bisect
N,M,K = map(int,input().split())
a_list = np.array([0]+list(map(int,input().split())))
b_list = np.array(list(map(int,input().split())))


a_list = a_list.cumsum()
b_list = b_list.cumsum()

max_cnt = 0
for i in range(N+1):
    if a_list[i]>K:
        continue
    cnt = i
    bT = K - a_list[i] + 1
    cnt += bisect.bisect_left(b_list,bT)
    if cnt >max_cnt:
        max_cnt = cnt

print(max_cnt)


