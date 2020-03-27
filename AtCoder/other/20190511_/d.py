import math
import numpy as np
N = int(input())
m_list = []
max_p = math.floor(-1+math.sqrt(1+N))
for p in range(1, max_p+1):
   if N % p == 0:
       m = N//p -1
       m_list.append(m)
print(int(np.sum(m_list)))