import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A,reverse=True)

happiness_list = [0]
# happiness = 0

# for i in range(M):
#     pos_left = 0
#     happiness+= A[pos]


for i in range(N):
    for j in range(N):
        power = A[i]+A[j]
        insert_index = bisect.bisect_left(happiness_list,power)
        happiness_list.insert(insert_index,power)

ans = sum(happiness_list[-M:])
print(ans)

# maxnum = 2 * max(A)
# happydic = [0]*(maxnum + 1)
# happydic = {}
# for i in range(N):
#     for j in range(N):
#         if A[i]+A[j] in happydic.keys():
#             happydic[A[i]+A[j]]+=1
#         else:
#             happydic[A[i]+A[j]] = 1
# left = M
# happiness = 0

# for val in sorted(happydic.keys(), reverse = True):
#     if left > 0:
#         temp = min(left, happydic[val])
#         happiness += temp * val
#         left -= temp
#     else:
#         if left == 0:
#             print(happiness)
#             break