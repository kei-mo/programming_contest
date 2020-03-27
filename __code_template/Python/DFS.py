def dfs(graph,start):
    '''
    args
    graph: 
    start: 
    '''
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
        return visited

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # visited の初期化
    visited.add(start)
    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited)
    return visited