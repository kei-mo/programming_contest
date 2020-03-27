A,B,M = map(int,input().split())
a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))

min_cost = min(a_list)+min(b_list)
for _ in range(M):
    x,y,c = map(int,input().split())
    cost = a_list[x-1] + b_list[y-1] -c
    if cost<min_cost:
        min_cost = cost
print(min_cost)