import numpy as np
N, Q= map(int,input().split())
const_list = []
for _ in range(N):
    const_list.append(list(map(int,input().split())))

const_list = np.array(const_list)
const_list = const_list[np.argsort(const_list[:,2])]
start = const_list[:,0] - const_list[:,2]
end = const_list[:,1] - const_list[:,2] - 1
spe = start+end
se = start*end

for _ in range(Q):
    q = int(input())
    check = q*q + se - spe * q
    true_index_list = np.where(check>=0)[0]
    if len(true_index_list)==0:
        print(-1)
    else:
        print(const_list[:,2][true_index_list[0]])
