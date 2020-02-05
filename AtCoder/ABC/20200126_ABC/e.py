import numpy as np 
H, N = map(int, input().split())
a_list = []
b_list = []

best_at_a = None
best_at_b = None
best_at_c = 0

for _ in range(N):
    a,b =  map(int, input().split())
    a_list.append(a)
    b_list.append(b)
    
    c = a/b # コスパ
    if c>best_at_c:
        best_at_c=c
        best_at_a=a
        best_at_b=b
a_list = np.array(a_list)
b_list = np.array(b_list)


rest_hp = H%best_at_a
attack_num = H//best_at_a


# def dp(hp,cost,min_cost):
#     if hp<0:
#         if cost<min_cost:
#             min_cost = cost
    
#     else:
#         for i in range(N):
#             min_cost= dp(hp-a_list[i], cost+b_list[i],min_cost)
#             if 
#     return min_cost

# def knapsack(N,W,weight,value):
#   #初期化
#   inf=float("inf")
#   dp=[[inf for i in range(W+1)] for j in range(N+1)]
#   for i in range(W+1): 
#       dp[0][i]=0

#   #DP
#   for i in range(N):
#     for w in range(W+1): # wは削ったコスト
#       if weight[i]<=w: #dp[i][w-weight[i]の状態にi番目の荷物が入る可能性がある
#         dp[i+1][w]=min(dp[i][w-weight[i]]+value[i], dp[i][w])
#       else: #入る可能性はない
#         dp[i+1][w]=dp[i][w]
#   return dp[N][W]




if rest_hp>0:
    max_attack_num = rest_hp//np.min(a_list)+1
    dp = [0 for _ in range(max_attack_num)]
    for i in range(max_attack_num):
        rest_hp_before = rest_hp

        # 次回以降倒す場合、最もコストパフォーマンスが良い攻撃
        bool_list = a_list<rest_hp
        if sum(bool_list)!=0:
            a_list_tmp = a_list[bool_list]
            b_list_tmp = b_list[bool_list]
            c = np.argmax(a_list_tmp/b_list_tmp)
            rest_hp -= a_list_tmp[c]
            dp[i+1] += dp[i]+b_list_tmp[c]

        # 今回倒す場合　倒せる中で最もコストの低い攻撃
        dp[i] = dp[i] + np.min(b_list[a_list>=rest_hp_before])
        
    last_attack_cost = min(dp)
else:
    last_attack_cost=0

ans = attack_num*best_at_b + last_attack_cost
print(ans)