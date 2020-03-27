N = int(input())
h_list = list(map(int,input().split()))

INF = 100001001010000
dp = [INF]*N # dp[i]:足場iに行くまでの最小コスト
dp[0] = 0
dp[1] = abs(h_list[1] - h_list[0])

for i in range(2,N):
    s0 = dp[i-2] + abs(h_list[i]-h_list[i-2]) # 2つ前の足場から飛ぶ場合
    s1 = dp[i-1] + abs(h_list[i]-h_list[i-1]) # 1つ前の足場から飛ぶ場合
    dp[i] = min(s0,s1) # コストが少ない方を選ぶ

print(dp[N-1])    