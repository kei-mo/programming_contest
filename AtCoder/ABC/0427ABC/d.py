import numpy as np
N = int(input())
A_list = list(map(int,input().split()))
neg_num = len([x for x in A_list if x<0])
zero_num = len([x for x in A_list if x==0])
abs_list = [abs(x) for x in A_list]

ans = np.sum(abs_list)
if neg_num%2==0 or zero_num>0:
    ans = ans
elif neg_num%2!=0:
    ans = ans - 2*min([x for x in abs_list if x!=0])
print(ans)