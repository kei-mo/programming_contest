N = int(input())

happiness = list(map(int,input().split()))
dp = happiness # dp: i日目にa~cそれぞれの活動をしたときの幸福度の最大値

for i in range(1,N):
    happiness = list(map(int,input().split()))
    dp_pre = dp

    dp[0] = max(dp_pre[1],dp_pre[2])+happiness[0] # i日目にaをする場合
    dp[1] = max(dp_pre[0],dp_pre[2])+happiness[1] # i日目にbをする場合
    dp[2] = max(dp_pre[1],dp_pre[0])+happiness[2] # i日目にcをする場合
     
print(max(dp))
