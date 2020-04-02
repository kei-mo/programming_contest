


# 隣接行列を使った場合
def dijkstra(n,graph,s):
    # n: ノード数
    # graph: 隣接行列 (n,n)
    # s: 基準となるノード ノードsからの最短距離を求める
    
    d = [float('inf')] * n # ノードsからの距離
    d[s] = 0 
    notvisited = [True] * n
    
    while True:

        # 次に基準となる頂点をみつける
        # 決定していない頂点の中で最も近い頂点をみつける (これはこれ以上近くならない) 
        vertex = -1
        for i in range(n): 
            if (notvisited[i] and vertex==-1):
                vertex = i
            elif (notvisited[i] and d[i]<d[vertex]):
                vertex = i
        if vertex==-1: # すべての頂点を決定した
            break 
        notvisited[vertex] = False

        # 基準となる頂点をもとにsからの最短距離を更新する
        for j in range(n):
            d[j] = min(d[j],d[vertex]+graph[vertex][j])

    return d

import heapq
# heapを使った場合
def dijkstra(n:int,graph:dict,s): -> list
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