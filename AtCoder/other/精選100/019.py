import bisect

d = int(input())
n = int(input())
m = int(input())
d_list = [0]
for _ in range(n-1):
    d_list.append(int(input()))
d_list.append(d)
d_list.sort()

k_list = []
for _ in range(m):
    k_list.append(int(input()))
ans = 0

for i in range(m):
    k = k_list[i]
    r_store = bisect.bisect_right(d_list,k) 
    l_store = r_store - 1
    ans += min(k-d_list[l_store],d_list[r_store]-k)
print(ans)