N,M = map(int,input().split())

a_list = []
for i in range(N):
    a_list.append(list(map(int,input().split())))

max_point = 0
for i in range(M-1):
    for j in range(i+1,M):
        point =0
        for n in range(N):
            point+=max(a_list[n][i],a_list[n][j])
        if point>max_point:
            max_point=point
print(max_point)
