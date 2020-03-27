
from collections import deque
import numpy as np

N = int(input())
graph = {i:[] for i in range(N)}
for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

# グラフのうち最も遠い2点の距離(木の直径)を求める
# 1. 適当な点からの最も遠い点uを求める
# 2. uから最も遠い点を求める
# 全探索×2

def bfs(graph,root):
    distance  = [0]*N
    visited = set()
    queue = deque([root])
    while len(queue) > 0:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                distance[neighbour] = distance[vertex] + 1
                visited.add(neighbour)
                queue.append(neighbour)

    farthest_node = np.argmax(distance)
    farthest_dist = distance[farthest_node]
    return farthest_node, farthest_dist

u, _ = bfs(graph, root=0)
_, diamiter = bfs(graph, root=u)

if diamiter%3==1:
    ans = 'Second'
else:
    ans = 'First'
print(ans)