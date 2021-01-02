import numpy as np
N = int(input())
priority_dict = {}
ans = 0
aN=0
bN = 0

ab_list = []

for i in range(N):
    a,b = map(int,input().split())
    aN += a
    # ab_list.append()
    c = a+b
    if c in priority_dict:
        priority_dict[c].append([a,b])
    else:
        priority_dict[c] = [[a,b]]



c_list = np.array(list(priority_dict.keys()))
priority_list = np.argsort(- c_list)

for i in priority_list:
    c = c_list[i]
    ab = np.array(priority_dict[c])
    a_order = np.argsort(- ab[:,0]) # aが多い順
    for j in a_order:
        ans+=1
        a = ab[j,0]
        b = ab[j,1]
        aN -= a
        bN += b + a
        if bN>aN:
            print(ans)
            break
    if bN>aN:
        break


