N,W = map(int,input().split())

dp = [0]*(W+1) # dp[i][w]はi個までの品物を使い、w以下の重さ分詰めたときの価値の最大値

for i in range(N):
    w,v = map(int,input().split())
    for j in range(W+1)[::-1]:
        if j>=w:
            dp[j] = max(dp[j],dp[j-w]+v)
        else:
            dp[j] = dp[j]

print(dp[-1])