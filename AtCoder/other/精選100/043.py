from collections import Counter
import numpy as np 

N = int(input())

s_matrix = []
for _ in range(5):
    s_matrix.append(list(input()))
s_matrix = np.array(s_matrix)
c_dict = {0:'R',1:'B',2:'W'}
c_list = [0,1,2]
INF = 1000100010001000100010000100010001000100010001000

# dp[i][j] : i行目を色jで塗るときの最小コスト
dp = [[INF for _ in range(3)] for _ in range(N+1)]
dp[0][:] = [0,0,0]

for i in range(1,N+1):
    c_counts = Counter(s_matrix[:,i-1])
    for j in range(3):
        c = c_dict[j]
        if c in c_counts:
            cost = 5- c_counts[c]
        else:
            cost = 5

        # i-1のjの色以外から遷移する
        pre_cost = []
        for k in range(3):
            if k!=j:
                pre_cost.append(dp[i-1][k])
        
        dp[i][j] = min(pre_cost) + cost
        
print(min(dp[-1][:]))