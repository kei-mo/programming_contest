#問題D
# Not correct

#M,N = list(map(int,input().split())) 
#ROW = list(map(int,input().split())) 
#COL = list(map(int,input().split())) 
# ROW = [8,9,7]
# COL = [6,9,8]
ROW = [158, 167, 181, 147, 178, 151, 179, 182, 176, 169, 180, 129, 175, 168]
COL = [181, 150, 178, 179, 167, 180, 176, 169, 182, 177, 175, 159, 173]
N = len(ROW)
M = len(COL)
import numpy as np
row = 0
col = 0
nums = np.arange(1,M*N+1)[::-1]
pattern = np.zeros(M*N)
#print(nums)
for i in nums:
    if i in ROW and i in COL:
        row += 1
        col += 1
        pattern[i-1] = 1
    elif i in ROW and i not in COL:
        row += 1
        pattern[i-1] = col
    elif i not in ROW and i in COL:
        col += 1
        pattern[i-1] = row
    elif i not in ROW and i not in COL:
        pattern[i-1] = row * col - (M*N-i)
        if pattern[i-1] <= 0:
            pattern[i-1] = 0
            break
    print(i,row,col,pattern[i-1])
print(pattern)
ans = int(pattern.prod())
ans = ans % (10**9+7)
print(ans)