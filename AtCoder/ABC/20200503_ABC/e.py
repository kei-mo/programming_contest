from collections import Counter

N = int(input())
alist = list(map(int, input().split()))
alist = [0] + alist
sumlist = []
# (j, wj)のリストを作る
for i in range(1,N+1):
    sumlist.append(i+alist[i])
sumlist.sort()
sum_cnt = Counter(sumlist)
ans = 0
# 差と一致するものを探す
for i in range(1, N+1):
    diff = i - alist[i]
    if diff in sum_cnt:
        ans += sum_cnt[diff]
print(ans)