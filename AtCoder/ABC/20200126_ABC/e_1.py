import numpy as np 
H, N = map(int, input().split())
a_list = []
b_list = []

rest_hp = H

for _ in range(N):
    a,b =  map(int, input().split())
    a_list.append(a)
    b_list.append(b)
    
a_list = np.array(a_list)
b_list = np.array(b_list)


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
    bool_list =  a_list>=rest_hp_before
    if sum(bool_list)==0:
        dp[i]=np.inf
    else:
        dp[i] = dp[i] + np.min(b_list[bool_list])

print(min(dp))