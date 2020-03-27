H,W = map(int,input().split())
mod = 1000000007

a_matrix = []
for _ in range(H):
    a_matrix.append(list(input()))

dp = [[0 for w in range(W+1)] for h in range(H+1)]

dp[1][0] = 1

for w in range(1,W+1):
    for h in range(1,H+1):
        if a_matrix[h-1][w-1] == ".":
            dp[h][w] = (dp[h-1][w] + dp[h][w-1]) % mod
        else:
            dp[h][w] = 0
print(dp[H][W])
        

