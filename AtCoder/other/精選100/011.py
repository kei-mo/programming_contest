#ABC 128 C Switches
import numpy as np 
N,M = map(int,input().split())
# switch_matrix = np.ones((M,N))
switch_list = []
for m in range(M):
    inputs = list(map(int,input().split()))
    k = inputs[0]
    s_list = inputs[1:]
    p = 0
    for s in s_list:
        p= p | pow(2,s-1)

    switch_list.append(p)
p_list = list(map(int,input().split()))

ans=0
for i in range(pow(2,N)):
    num = 0
    for m in range(M):
        a = bin(i & switch_list[m]).count("1")
        if a%2 == p_list[m]:
            num+=1
    if num==M:
        ans+=1
print(ans)