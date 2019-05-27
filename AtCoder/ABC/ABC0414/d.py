N, K = map(int,input().split())
S= input()

# 連続している数を調べる
# 先頭は1とする
cont_list = []
now = '1'
cnt = 0

for s in S:
    if s == now:
        cnt += 1
    else:
        cont_list.append(cnt)
        now = s
        cnt = 1
cont_list.append(cnt)

# 最後も1にしたい
# 0の場合は
if S[:-1] == '0':
    cont_list.append(0)

sum_list = []
for i in range(0,N,2):
    tmp = cont_list[i] - 

