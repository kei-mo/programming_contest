from collections import Counter

N = int(input())
s_count = Counter([input() for _ in range(N)])
M = int(input())
t_count = Counter([input() for _ in range(M)])

s_count.subtract(t_count)
print(max(0,s_count.most_common(1)[0][1]))
