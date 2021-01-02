import numpy as np
N = int(input())
a_list = []
b_list = []
c_list = []

for i in range(N):
    a,b = map(int,input().split())
    c = a+b
    a_list.append(a)
    b_list.append(b)
    c_list.append(c)

a_list = np.array(a_list)
b_list = np.array(b_list)
c_list = np.array(c_list)

ans = 0
aN = np.sum(a_list)
bN = 0

priority_list = np.argsort(- c_list)

for i in priority_list:
    ans+=1
    aN -= a_list[i]
    bN += b_list[i] + a_list[i]
    if bN>aN:
        print(ans)
        break


