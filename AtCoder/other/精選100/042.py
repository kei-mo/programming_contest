N,M = map(int,input().split())
d_list = [0]
for _ in range(N):
    d_list.append(int(input()))

c_list = [0]
for _ in range(M):
    c_list.append(int(input()))

# dp[i][j] : i都市にて、これまでの旅でj回待機したときの最小コスト

INF = 1000100010001000100010001000

max_rest = M-N

dp = [[INF for _ in range(max_rest+2)] for _ in range(N+2)]
dp[0][1] = 0
dp[1][0] = 0

for i in range(1,N+2):
    for j in range(1,max_rest+2):
        # i-1都市目から移動してくる場合
        day = i-1 + j-1

        c = c_list[day]
        d = d_list[i-1]
        cost0 = dp[i-1][j] + c*d

        # i都市目で待機する場合        
        cost1 = dp[i][j-1]

        dp[i][j] = min(cost0,cost1)

print(dp[-1][-1])
