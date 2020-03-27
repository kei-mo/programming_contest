import heapq
import numpy as np 

N,M = map(int,input().split())

ab_list = []
for _ in range(N):
    a,b = map(int,input().split())
    ab_list.append([a,b])
ab_list = np.array(ab_list)
ab_list = ab_list[np.argsort(ab_list[:,0])]

ans = 0
h = []
# heapq.heapify(h)
flag = 0
for i in range(1,M+1):
    while flag<N:
        a = ab_list[flag][0]
        if a >i:
            break
        else: # 終了日までに報酬がももらえる
            b = ab_list[flag][1]
            heapq.heappush(h,-1 * b)
            flag+=1
    if len(h) > 0:
        ans += -1 * heapq.heappop(h)
print(ans)
