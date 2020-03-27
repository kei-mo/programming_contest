import numpy as np
N,M,Q = map(int,input().split())
grid = np.zeros((N+1,N+1))
for _ in range(M):
    l,r = map(int,input().split())
    grid[l,r] += 1

grid = grid.cumsum(axis=0).cumsum(axis=1)

for _ in range(Q):
    p,q = map(int,input().split())
    ans = grid[q,q] - grid[p-1,q] - grid[q,p-1] + grid[p-1,p-1]
    print(int(ans))
