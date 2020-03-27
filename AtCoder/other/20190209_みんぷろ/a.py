N, K = map(int,input().split())
if N>=(K-1)*2 + 1:
    ans = 'YES'
else:
    ans = 'NO'
print(ans)