import itertools
N = int(input())
p_list = tuple(map(int,input().split()))
q_list = tuple(map(int,input().split()))

pattern_list = list(itertools.permutations(range(1,N+1))) # 順列の生成

cnt = 1
for pattern in pattern_list:
    if pattern == p_list:
        a = cnt
    if pattern == q_list:
        b = cnt
    cnt+=1


print(abs(a-b))

