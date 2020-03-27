import bisect

N = int(input())

INF= 10**10+1

dp = [INF]*N # dp[i]:=i長の増加部分列を作るときに、使う最大値

for _ in range(N):
    c = int(input())
    in_pos = bisect.bisect_left(dp,c)
    dp[in_pos] = c

ans =N- bisect.bisect_left(dp,INF-1)
print(ans)