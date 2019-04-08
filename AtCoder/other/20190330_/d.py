import copy
import math

N, X = map(int,input().split())
S_list = list(map(int,input().split()))
mod = 10**9 + 7

ans = 0

def DFS(x,s_list):
    global ans
    if len(s_list) ==0:
        ans = (ans + x) % mod
    elif x < min(s_list):
        ans = (ans + x*math.factorial(len(s_list))) % mod
    # elif x in s_list:
    #     ans += 0
    else:
        s_list.sort(reverse=True)
        for i,s in enumerate(s_list):
             s_list_after = copy.deepcopy(s_list)
             s_list_after.pop(i)
             x_after = x%s
             DFS(x_after,s_list_after)
    
DFS(X,S_list)
print(ans% mod)