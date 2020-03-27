import heapq

class Dijkstra:
    def __init__(self,graph:dict,start,goal=None):
        # graph [dict]: グラフの情報
        
        self.graph = graph
        self.start = start
        self.goal = goal
        self.num_node = len(self.graph)
    
    def search(self):
        self.dist = [float("inf") for _ in range(self.num_node)]
        self.prev = [float("inf") for _ in range(self.num_node)]

        self.dist[start] = 0

        heap_q = []
        heapq.heappush(heap_q,(0,self.start))
        while len(heap_q)!=0:
            pass 

    def get_path(self,goal,prev):
        pass