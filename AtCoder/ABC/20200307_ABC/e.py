import numpy as np
N = int(input())

in_dict = {}

for _ in range(N):
    x,d = map(int,input().split())
    in_dict[x] = d
x_list = list(in_dict.keys())
d_list = list(in_dict.values())

in_dict = sorted(in_dict.items(), key=lambda x:x[0])

dp = [[0, for _ in range(N)] 
dp[0] = 2
move = np.array([d_list[0]])

for i in range(1,N):
    move = move -1 
    move = move[move>0]
    dp[i] = (dp[i-1] - len(move)**2)  + dp[i-1]
    dp[i] = dp[i]%998244353
    
    np.append(move,d_list[i])

print(dp[-1]%998244353)


    

    
