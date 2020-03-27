N = int(input())
bottle_neck = 10**15+10
for _ in range(5):
    bottle_neck = min(bottle_neck,int(input()))
ans = 5
if bottle_neck<N:
    ans += N//bottle_neck
if N%bottle_neck==0:
    ans -= 1
print(ans)