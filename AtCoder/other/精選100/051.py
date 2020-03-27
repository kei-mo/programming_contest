N = int(input())
MOD= 10007

resp_list = list(input())
member = {'J':0,'O':1,'I':2}
pattern_dict = {i:0 for i in range(1,8)}
#パターンをbitで管理

dp = [pattern_dict.copy() for i in range(N)]

# 1日め
r = member[resp_list[0]]
for i in pattern_dict.keys():
    if i & 1<<r == 1<<r:
        if i & 1<<0 == 1<<0:
            dp[0][i]=1
        

for i in range(1,N):
    # 前の日からの遷移を考える
    r = member[resp_list[i]] # 責任者   
    for j in pattern_dict.keys():
        if j & 1<<r == 1<<r: # 責任者がいるか
            for k in pattern_dict.keys():
                if j & k != 0: # 前日と今日で同じ参加者がいる
                    dp[i][j] += dp[i-1][k] % MOD
print(sum(dp[-1].values()) % MOD)

