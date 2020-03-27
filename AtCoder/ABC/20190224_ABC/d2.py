## TLE
import numpy as np
A, B, Q = map(int,input().split())
s_list = np.array([int(input()) for i in range(A)])
t_list = np.array([int(input()) for i in range(B)])
x_list = np.array([int(input()) for i in range(Q)])

def get_dist_to_first_cp(x,li):
    dist1 = li -x
    abs_dist1 = abs(dist1)
    dist_to_first_cp = min(abs_dist1)
    first_cp_num = np.argmin(abs_dist1)
    first_cp_pos = x + dist1[first_cp_num]
    return dist_to_first_cp, first_cp_pos
    
u_list = np.hstack((s_list,t_list))
for x in x_list:
    # shrine first
    dist_to_first_cp, first_cp_pos = get_dist_to_first_cp(x,s_list)
    dist2 = abs(np.array(t_list) - first_cp_pos)
    dist_to_sec_cp = min(dist2)
    ans_s = dist_to_first_cp + dist_to_sec_cp
    # temple first
    dist_to_first_cp, first_cp_pos = get_dist_to_first_cp(x,t_list)
    dist2 = abs(np.array(s_list) - first_cp_pos)
    dist_to_sec_cp = min(dist2)
    
    ans_t = dist_to_first_cp + dist_to_sec_cp

    print(min(ans_s,ans_t))
