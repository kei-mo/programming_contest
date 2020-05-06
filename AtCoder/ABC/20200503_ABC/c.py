import numpy as np 
N, M = map(int,input().split())
h_list = np.array(list(map(int,input().split())))

max_neigh_hight = np.zeros(N) # 隣接する展望台で最も高いもの

for _ in range(M):
    a,b = map(int,input().split())
    a-=1
    b-=1
    max_neigh_hight[a] = max(max_neigh_hight[a],h_list[b])
    max_neigh_hight[b] = max(max_neigh_hight[b],h_list[a])

diff = h_list - max_neigh_hight
ans = np.sum(diff>0)
print(ans)
