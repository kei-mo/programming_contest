N,D = map(int,input().split())


def factor(d,x):
    c = 0
    while d%x==0:
        d //= x
        c+=1
    return d,c

d, F2 = factor(D,2)
d, F3 = factor(d,3)
d, F5 = factor(d,5)

if d!=1:
    print(0)
    exit() 

dp = [[[[0 for _ in range(F5+1)] for _ in range(F3+1)] for _ in range(F2+1)] for _ in range(N+1)]  # dp[i][k,l,m]

dp[0][0][0][0] = 0

for i in range(N):
    for f2 in range(F2+1):
        for f3 in range(F3+1):
            for f5 in range(F5+1):
                dp[i+1][f2][f3][f5]   = dp[i][f2][f3][f5]+1 # 1
                dp[i+1][min(F2,f2+1)][f3][f5] = dp[i][f2][f3][f5] + 1 # 2
                dp[i+1][f2][min(F3,f3+1)][f5] = dp[i][f2][f3][f5] + 1 # 3
                dp[i+1][min(F2,f2+2)][f3][f5] = dp[i][f2][f3][f5] + 1 # 4
                dp[i+1][f2][f3][min(F5,f5+1)] = dp[i][f2][f3][f5] + 1 # 5
                dp[i+1][min(F2,f2+1)][min(F3,f3+1)][f5] = dp[i][f2][f3][f5] + 1 # 6

ans = dp[-1][-1][-1][-1]/6**N
print(ans)


