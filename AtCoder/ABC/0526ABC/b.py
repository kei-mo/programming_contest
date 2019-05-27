import numpy as np
N= int(input())
s_list = []
p_list = []
for _ in range(N):
    s, p = input().split()
    s_list.append(s)
    p_list.append(int(p))

s_unique = list(set(s_list))
s_unique.sort()
for s in s_unique:
    ps = []
    indexs = [i for i,x in enumerate(s_list) if x==s]
    for index in indexs:
        ps.append(p_list[index])
    ps_sorted_index = np.argsort(ps)[::-1]
    for i in ps_sorted_index:
        print(indexs[i]+1)

