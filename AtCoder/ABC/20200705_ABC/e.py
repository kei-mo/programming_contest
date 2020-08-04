from bisect import bisect_left

N,K = map(int,input().split())
a_list = list(map(int,input().split()))
a_list.sort()
b_list = a_list[-K:]

n_negative = bisect_left(a_list,0)

max_pair_num = min(n_negative//2, K//2)


# 負の数からiペア取る
n_product = 1
p_product = 1
for i in range(K):
    p_product*= b_list[i]

ans = p_product
for i in range(1,max_pair_num+1):
    n_product *= a_list[i*2-2]
    n_product *= a_list[i*2-1]

    p_product /= b_list[i*2-2]
    p_product /= b_list[i*2-1]

    if n_product*p_product>ans:
        ans = n_product*p_product

print(int(ans%1_000_000_007))

