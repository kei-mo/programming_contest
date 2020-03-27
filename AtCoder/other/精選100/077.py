n,m = map(int,input().split())
n_list = [1]
pos=1
for _ in range(n-1):
    pos+=int(input())
    n_list.append(pos)
m_list = []

cur_town = 1
total_dist = 0
MOD = 100000
for _ in range(m):
    next_town = cur_town + int(input())
    total_dist += abs(n_list[cur_town-1]- n_list[next_town-1])
    total_dist %= MOD
    cur_town=next_town
print(total_dist)