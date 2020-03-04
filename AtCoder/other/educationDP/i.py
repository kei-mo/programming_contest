N = int(input())
p_list = list(map(float,input().split()))

dp = [[0 for i in range(N+1)] for j in range(N)] # dp[i][j] i個降ったときにj個表になる確率

dp[0][0] = 1- p_list[0]
dp[0][1] = p_list[0]

for i in range(1,N):
    for j in range(1,N+1):
        dp[i][j] += dp[i-1][j-1] * p_list[i]   # 表が出る場合
        dp[i][j] += dp[i-1][j] * (1-p_list[i]) # 裏が出る場合
ans = sum(dp[-1][int(j/2):])
print(ans)