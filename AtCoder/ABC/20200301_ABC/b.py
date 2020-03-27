import numpy as np

a_matrix = []
for i in range(3):
    a_matrix.extend(list(map(int,input().split())))
flag_list = [0 for i in range(9)]

N = int(input())
for i in range(N):
    b = int(input())
    if b in a_matrix:
        pos = a_matrix.index(b)
        flag_list[pos] = 1

ans = 'No'
flag_matrix = np.array(flag_list).reshape(3,3)
for i in range(3):
    c = sum(flag_matrix[:,i])
    d = sum(flag_matrix[i,:])
    if (c==3 or d==3):
        ans = 'Yes'

c = flag_matrix[0,0]+flag_matrix[1,1]+flag_matrix[2,2]
d = flag_matrix[0,2]+flag_matrix[1,1]+flag_matrix[2,0]
if (c==3 or d==3):
    ans = 'Yes'
print(ans)
