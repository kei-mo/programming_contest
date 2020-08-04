N = int(input())
a_list = map(int,input().split())

ans = 1
for a in a_list:
    ans *= a
    if ans > 10**18:
        ans = -1
        break
    
if 0 in a_list:
    ans = 0
print(ans)

