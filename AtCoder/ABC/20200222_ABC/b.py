N, K = map(int,input().split())
n = N
# if n ==1:
#     ans =1
# else:
#     while n>1:
#         n = n/K
#         ans+=1

ans =1
while n>=K:
    n = n//K
    ans +=1

print(ans)