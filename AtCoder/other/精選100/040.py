import numpy as np

N,K = map(int,input().split())
d =dict()
for _ in range(K):
    a,b = input().split()
    d[a] = int(b)

dp = np.ones((3,3))
if "1" in d:
    i = d["1"] - 1
    a = [0,1,2]
    a.remove(i)
    for j in a:
        dp[j,:] = 0
if "2" in d:
    i = d["2"] - 1
    a = [0,1,2]
    a.remove(i)
    for j in a:
        dp[:,j] = 0



for n in range(3,N+1):    
    dp_pre = dp.copy()
    if str(n) in d:
        i = d[str(n)]-1
        a = [0,1,2]
        a.remove(i)
        dp[i,i] = sum(dp_pre[:,i]) - dp_pre[i,i]
        for j in a:
            dp[j,i] = sum(dp_pre[:,j]) 
            dp[:,j] = 0
    else:
        for i in [0,1,2]:
            dp[i,i] = sum(dp_pre[:,i]) -dp_pre[i,i] # 対角線
            a = [0,1,2]
            a.remove(i) 
            for j in a: # 対角線以外
                dp[j,i] = sum(dp_pre[:,j])
                dp[j,i] = sum(dp_pre[:,j])
    dp = dp % 10000
ans = np.sum(dp)  % 10000
print(int(ans))