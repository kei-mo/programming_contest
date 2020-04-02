import heapq

def dijkstra(n:int,graph_a:dict,graph_b,s): -> list
    # n: ノード数
    # graph: エッジの {x0:[(w1,y1),(w2,y2),...],x1:[...]} リストの中はタプルにする
    # s: 基準となるノード ノードsからの最短距離を求める
    
    d = [float('inf')] * n  # ノードsからの距離
    notvisited = [True] * n # 訪れていない、すなわち決定していない頂点
    vertex_list = []        # 次に訪れる頂点の候補リスト

    # sに合わせて初期化
    d[s] = 0
    [heapq.heappush(vertex_list,v) for v in graph[s]] # 候補リストの初期化

    while len(vertex_list):
        minedge = heapq.heappop(vertex_list) # 決定していない頂点のうちsからの距離が最小のものを基準とする
        vertex = minedge[1]
        if notvisited[vertex]:
            d[vertex] = minedge[1]
            notvisited[vertex] = False # 距離決定

            # 基準となる頂点からと連結している頂点をみて、次の頂点の候補リストを更新
            for e in graph[vertex]: 
                next_vertex = e[1]
                if notvisited[next_vertex]:
                    heapq.heappush(vertex_list,(d[vertex]+e[0],next_vertex)) # 候補リストに頂点を追加
    
    return d



n,m,s,t = map(int,input().split())
graph_a = {x:[] for x in range(1,n+1)}
graph_b = {x:[] for x in range(1,n+1)}

for _ in range(m):
    u,v,a,b = map(int,input())
    graph_a[u].append((a,v))
    graph_a[v].append((a,u))
    graph_b[u].append((b,v))
    graph_b[v].append((b,u))