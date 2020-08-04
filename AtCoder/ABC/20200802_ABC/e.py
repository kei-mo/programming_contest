import math

N, K = map(int, input().split())
a_list = list(map(int, input().split()))

K += N
sum_ = sum(a_list)

ideal_d = [(K / sum_) * a for a in a_list]
min_d = [math.floor(i_d) if math.floor(i_d) != 0 else 1 for i_d in ideal_d]

max_ded_a_list = [a/m_d for a, m_d in zip(a_list, min_d) ]
min_ded_a_list = [a/(m_d+1) for a, m_d in zip(a_list, min_d)]
num_replace = K - sum(min_d)
max_ded_a_list.sort(reverse=True)

ans = math.ceil(max_ded_a_list[num_replace])
print(ans)