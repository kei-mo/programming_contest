import numpy as np 

def solve():
    C,D = map(int,input().split())
    order = list(map(int,input().split()))
    order_dict = {} # i番目に到達する
    for i, t in enumerate(order):
        if -t in order_dict:    
            order_dict[-t].append(i+2)
        else:
            order_dict[-t] = [i+2]
    
    graph = {i:{} for i in range(1,C+1)}
    ans_order = []
    for _ in range(D):
        a,b = map(int,input().split())

        graph[a][b] = 1
        graph[b][a] = 1

        ans_order.append((a,b))

    # order = np.argsort(order)
    latency = 0
    finished = {1:0} # k:t ノードkが終わった時間t
    for t,v in order_dict.items():
        latency = t # t病後に到着   
        for i in v:
            for k in graph[i]:
                if k in finished:
                    tau =  max(1,latency - finished[k] )
                    graph[i][k] = tau
                    graph[k][i] =  tau
            finished[i] = latency
    
    ans= ""
    for x in ans_order:
        ans += str(graph[x[0]][x[1]])+" "
    return ans[:-1]


T = int(input())

for n in range(1,T+1):
    ans = solve()

    print('Case #'+str(n)+': '+ ans)
