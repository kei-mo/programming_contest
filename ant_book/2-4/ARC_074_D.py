import heapq
import numpy as np 

N = int(input())
a_list = list(map(int,input().split()))

bound = N # 前後の境
h_pre = a_list[:N]
h_post = [-1 * a for a in a_list[2*N:]]
heapq.heapify(h_pre ) 
heapq.heapify(h_post ) 

pre_sum = np.zeros((N+1,1))
post_sum = np.zeros((N+1,1))
pre_sum[0] = sum(h_pre)
post_sum[-1] = -1 *  sum(h_post)

for i in range(N):
    a = a_list[N+i]
    small = heapq.heappushpop(h_pre,a)
    pre_sum[i+1] = pre_sum[i] + a - small
    
    b = a_list[-(i+N+1)]
    large = heapq.heappushpop(h_post,-1 * b)
    post_sum[N-(i+1)] = post_sum[N-i] + b + large


ans = np.max(pre_sum - post_sum)

print(int(ans))
        
    
