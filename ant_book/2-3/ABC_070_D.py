from collections import deque

def bfs(graph,root,distK):
    visited = set([root])       # 訪問済みノードを管理する 
    queue = deque([root]) # 訪れるべきノードを管理するqueueを作成
    while queue:          # list queueが空になるまで行う
        vertex = queue.popleft()         # 頂点を極める
        for neighbour in graph[vertex]:  # 頂点の近隣のノードに調べる
            node = neighbour[0]
            dist = neighbour[1]
            if node not in visited:
                visited.add(node)
                queue.append(node)
                distK[node] = distK[vertex] + dist
    return distK

N = int(input())
graph = {i:[] for i in range(1,N+1)}
for _ in range(N-1):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

Q,K = map(int,input().split())
distK = {K:0}
distK = bfs(graph,K,distK)
for _ in range(Q):
    x,y = map(int,input().split())
    print(distK[x] + distK[y])