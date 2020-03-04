import numpy as np
N = int(input())
x_list = list(map(int,input().split()))

pos = round(np.mean(x_list))
ans = sum([(x-pos)**2 for x in x_list])
print(int(ans))
