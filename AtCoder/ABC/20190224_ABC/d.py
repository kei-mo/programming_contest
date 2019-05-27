import numpy as np
# A, B, Q = map(int,input().split())
# s_list = [int(input()) for i in range(A)]
# t_list = [int(input()) for i in range(B)]
# x_list = [int(input()) for i in range(Q)]
A,B,Q = 2,3,4
s_list = [100,600]
t_list = [400,900,1000]
x_list = [150,2000,899,799]

def dist2_first_cp(x,li):
    dist1 
    

ans =  [0 for _ in range(Q)]

u_list = s_list + t_list
for i, x in enumerate(x_list):
    
    dist1 = [u-x for u in u_list] # スタート地点との距離
    abs_dist1 = list(map(abs,dist1))
    dist_to_first_cp = min(abs_dist1)

    ans[i] = ans[i] + dist_to_first_cp
    first_cp_num = np.argmin(abs_dist1)
    first_cp_pos = x + dist1[first_cp_num]
    if first_cp_num<A:
        first_cp_type = "s"  # 最初に訪れたのはshrine
    else:
        first_cp_type =  "t"


    if first_cp_type =="s": # 次の訪れるのはtemple
        dist2 = [t - first_cp_pos for t in t_list]
    else:
        dist2 = [s - first_cp_pos for s in s_list]
    dist_to_sec_cp = min(map(abs,dist2))
    ans[i] = ans[i] +  dist_to_sec_cp
    print(dist_to_first_cp,dist_to_sec_cp)

for i in range(Q):
    print(ans[i])
