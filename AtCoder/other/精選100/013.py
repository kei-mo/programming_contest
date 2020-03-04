import numpy as np 
R,C = map(int,input().split())
p_list = []
q_list=[]
bit_max = pow(2,C)-1
for _ in range(R):
    inputs = list(map(int,input().split()))
    p = 0
    for i in range(C):
        if inputs[i]==1:
            p = p | 1<<(C-i-1)
            
    p_list.append(list(format(p,"b").zfill(C)))
    q_list.append(list(format(~p&bit_max,"b").zfill(C)))

max_num = 0
for byte in range(pow(2,R)):
    num = 0
    p = format(byte,"b").zfill(R)
    u_list = []
    for r in range(R):
        if p[r]=="1": # 行をひっくり返す
            u_list.append(p_list[r])
        else:
            u_list.append(q_list[r])
    u_list = np.array(u_list,dtype='uint8') # 行をひっくり返したあとの状態
    u_list_sum = np.sum(u_list,axis=0)
    num = sum([max(R-s,s) for s in u_list_sum])
    if num>max_num:
        max_num=num
print(int(max_num))


