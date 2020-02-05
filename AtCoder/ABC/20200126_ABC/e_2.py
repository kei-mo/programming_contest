H, N = map(int, input().split())
inf =10*10
dp = [inf for _ in range(H+1)]

# min_cost = np.inf
dp[0]=0
for n in range(N):
    a,b =  map(int, input().split())
    for h in range(H):
        nj = min(h+a,H)
        dp[nj] = min([dp[nj],dp[h]+b])
        
print(int(dp[H]))





# for h in range(H): # h はこれまで削った体力
#     if dp[h]!=np.inf:
#         for n in range(N):

#             a= a_list[n]
#             b= b_list[n]
#             if h+a_list[n]<H:
#                 dp[h+a] = np.min([dp[h+a], dp[h]+b])
#             elif dp[h]+b<min_cost:


