L=int(input())
A=[int(input()) for _ in range(L)]
dp=[0 for _ in range(5)]
 
for a in A:
    back = a%2 if a>0 else 2
    through = (a+1)%2
 
    dp[4] = min(dp[0:5]) + a
    dp[3] = min(dp[0:4]) + back
    dp[2] = min(dp[0:3]) + through
    dp[1] = min(dp[0:2]) + back
    dp[0] = dp[0]+a
 
print(min(dp))