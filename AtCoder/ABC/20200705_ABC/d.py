import heapq

N = int(input())
a_list = list(map(int,input().split()))
a_list.sort(reverse=True)

ans = 0

conf_heap = []
heapq.heapify(conf_heap)
heapq.heappush(conf_heap,-1*a_list[0])

for i in range(1,N):
    ans += -1 * heapq.heappop(conf_heap)
    heapq.heappush(conf_heap,-1*a_list[i])
    heapq.heappush(conf_heap,-1*a_list[i])
print(ans)
