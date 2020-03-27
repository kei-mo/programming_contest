import numpy as np
N,M,C = map(int,input().split())
b_list = np.array(list(map(int,input().split())))

ans = 0
for i in range(N):
    a_list = np.array(list(map(int,input().split())))
    s = sum(a_list*b_list)+C
    if s > 0:
        ans += 1
print(ans)