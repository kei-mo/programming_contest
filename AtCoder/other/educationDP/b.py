# PyPyなら通った

N, K  = map(int,input().split())
h_list = list(map(int,input().split()))

INF = 100001010000100
dp = [INF]*N
dp[0] = 0

for i in range(1,N):
    start = max(0,i-K)
    dp[i] = min([dp[j]+abs(h_list[i]-h_list[j]) for j in range(start,i)]) # 1,...j,...K step前から飛んだ場合を計算しその最小値

print(dp[N-1])