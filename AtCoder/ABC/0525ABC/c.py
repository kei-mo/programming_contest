N, M = map(int,input().split())
l_list = []
r_list = []
for _ in range(M):
    l, r = map(int,input().split())
    l_list.append(l)
    r_list.append(r)

l_max = max(l_list)
r_min = min(r_list)
ans = max(0,r_min-l_max+1)
print(ans)