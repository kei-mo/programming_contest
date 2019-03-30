N = int(input())
XU = [input().split() for i in range(N)]

ans = 0.0 
for i in range(N):
    x = float(XU[i][0])
    u = XU[i][1]
    if u == 'JPY':
        ans += x
    else:
        ans += x * 380000.0

print(ans)￼