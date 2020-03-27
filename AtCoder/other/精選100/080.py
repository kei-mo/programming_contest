

import numpy as np

H,W,K,V = map(int,input().split())
grid = np.zeros((H+1,W+1))
for h in range(1,H+1):
    grid[h,1:] = np.array(list(map(int,input().split()))) + K 
grid = grid.cumsum(axis=0).cumsum(axis=1)

ans = 0
for y in range(1,H+1):
  for x in range(1,W+1):
    if y*x<=ans:
      continue
    costs=grid[y:,x:]-grid[:-y,x:]-grid[y:,:-x]+grid[:-y,:-x]
    if np.any(costs<=V):
      ans=y*x
      
print(ans)

# for a in range(0,H):
#     for c in range(a+1,H+1):
#         for b in range(0,W):
#             for d in range(b+1,W+1):
#                 area = (c-a)*(d-b) 
#                 h_cost = area* K
#                 l_cost =  grid[c,d] - grid[c,b] - grid[a,d] + grid[a,b]
#                 if h_cost+l_cost<=V:
#                     if area>max_area:
#                         max_area=area


