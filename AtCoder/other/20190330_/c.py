
N, Q = map(int,input().split())
s_list = list(input())
s_unique = list(set(s_list))
pos_dict = {}
for s in s_list:
    try:
        pos_dict[s] += 1
    except:
        pos_dict.update({s:1}) 
g_num_list = [1]*N

for i in range(Q):
    s_temp, direction = input().split()
    if s_temp in s_unique:
        pos_list = pos_dict[s_temp]
        for pos in pos_list:

            if direction=='L':
                if pos!=0:
                    g_num_list[pos-1] += g_num_list[pos]
            else:
                if pos!=N-1:
                    g_num_list[pos+1] += g_num_list[pos]
            g_num_list[pos] = 0
ans = sum(g_num_list)
print(ans)
            
