import numpy as np 

N,Q = map(int,input().split())
dp = np.zeros((N+1,N),dtype=np.uint16)
c_list = list(map(int,input().split()))
for i,c in enumerate(c_list):
    dp[i+1,:] = dp[i,:]
    dp[i+1,c-1] = dp[i+1,c-1] + 1

for _ in range(Q):
    l,r = map(int,input().split())
    print(np.sum(dp[r,:]-dp[l-1,:] >0))

