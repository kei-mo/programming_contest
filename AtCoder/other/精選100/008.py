import numpy as np
N= int(input())
a_list=[]
b_list=[]
for _ in range(N):
    a,b = map(int,input().split())
    a_list.append(a)
    b_list.append(b)

x = round(np.median(a_list))
y = round(np.median(b_list))

ans = 0
for i in range(N):
    a = a_list[i]
    b = b_list[i]
    ans+= abs(a-x) + b-a + abs(b-y)

print(int(ans))