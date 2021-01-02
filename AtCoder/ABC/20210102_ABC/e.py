N = int(input())

childs = {i:[] for i in range(1,N+1)}
parents = {i:[] for i in range(1,N+1)}

for i in range(N):
    a,b = map(int,input().split())
    childs[a].append(b)
    parents[b].append(a)

add_list = {i:0 for i in range(1,N+1)} # iの子供に足す
Q = int(input())





