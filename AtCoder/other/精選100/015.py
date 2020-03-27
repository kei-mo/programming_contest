import numpy as np 
import itertools
N = int(input())
pos = []
for _ in range(N):
    pos.append(list(map(int,input().split())))
pos = np.array(pos)

dist_dict = {}
def dist(n0,n1): # inputはノード番号
    k = str(min(n0,n1))+str(max(n0,n1))
    if k in dist_dict:
        d = dist_dict[k]
    else:
        d = np.sqrt(np.sum(np.power(pos[n1]-pos[n0],2)))
        dist_dict[k] =d
    return d

pattern_list = list(itertools.permutations(range(N))) # 順列の生成
ans = 0
for pattern in pattern_list:
    pre_node = pattern[0]
    for i in range(1,N):
        next_node = pattern[i]
        ans+=dist(pre_node,next_node)
        pre_node = next_node

for i in range(1,N+1):
    ans /= i

print(ans)