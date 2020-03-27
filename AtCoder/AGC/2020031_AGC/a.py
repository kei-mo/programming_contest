H,W = map(int,input().split())

INF = 10000000000

grid = [["." for _ in range(W+1)]]

for _ in range(H):
    in_list = list("." + input())
    grid.append(in_list)

# dp[i][j] = x x: これまでに何ブロックあったか
dp = [[INF for _ in range(W+1)] for _ in range(H+1)]
dp[1][0] = 0
dp[0][1] = 0


# if grid[0][0] = "#":
#     dp[0][0] = 1
# else:
#     dp[0][0] = 0

for j in range(1,W+1):
    for i in range(1,H+1):
        if grid[i][j] == ".": # 白の場合
            dp[i][j] = min(dp[i-1][j],dp[i][j-1])
        else: # 黒の場合
            # route_top
            if grid[i-1][j] == "#": # 上も黒ならそのまあ
                route_top = dp[i-1][j]
            else:
                route_top = dp[i-1][j] + 1

            # route_left
            if grid[i][j-1] == "#": # 上も黒ならそのまあ
                route_left = dp[i][j-1]
            else:
                route_left = dp[i][j-1] + 1
            
            dp[i][j] = min(route_top,route_left)
print(dp[-1][-1])