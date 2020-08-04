N,D = map(int,input().split())
DD = D*D

ans = 0
for i in range(N):
    x,y = map(int,input().split())
    if x*x + y*y <= DD:
        ans +=1

print(ans)
