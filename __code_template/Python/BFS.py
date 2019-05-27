from collections import deque

def bfs(graph,root):
    visited = set()       # 訪問済みノードを管理する 
    queue = deque([root]) # 訪れるべきノードを管理するqueueを作成
    while queue:          # list queueが空になるまで行う
        vertex = queue.popleft()         # 頂点を極める
        for neighbour in graph[vertex]:  # 頂点の近隣のノードに調べる
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


if __name__ == "__main__":
    graph = {0:[1,2], 1:[0,3], 2:[]}