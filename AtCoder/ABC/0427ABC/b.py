N = int(input())
v_list = list(map(int,input().split()))
c_list = list(map(int,input().split()))

ans = 0
for i in range(N):
    sub = v_list[i] - c_list[i]
    if sub>0:
        ans += sub
print(ans)