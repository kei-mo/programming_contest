import numpy as np

H,W=map(int,input().split())
max_value = H+W
matrix =[]

for _ in range(H):
    matrix.append([0 if i == '#' else max_value for i in list(input())])
matrix = np.array(matrix)

for c in range(W-1):
    matrix[:,c+1] = np.minimum(matrix[:,c]+1,matrix[:,c+1])
for c in range(W-1,0,-1):
    matrix[:,c-1] = np.minimum(matrix[:,c-1],matrix[:,c]+1)
for r in range(H-1):
    matrix[r+1,:] = np.minimum(matrix[r,:]+1,matrix[r+1,:])
for r in range(H-1,0,-1):
    matrix[r-1,:] = np.minimum(matrix[r,:]+1,matrix[r-1,:])
print(np.max(matrix))
