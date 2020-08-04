import numpy as np
import math
H,W,K = map(int,input().split())
m = []
for i in range(H):
    m.append(list(input()))
m = np.array(m)
bcell = m=="#"

ans = 0
for i in range(2**H):
    r_pattern = np.array(list(format(i, f'0{H}b')))=='1'
    for j in range(2**W):
        c_pattern = np.array(list(format(j, f'0{W}b')))=='1'
        mask = r_pattern.reshape(H,1) & c_pattern.reshape(1,W)
        
        b_cell_num = np.sum(bcell&mask)
        if b_cell_num ==K:
            ans +=1
print(ans)
        