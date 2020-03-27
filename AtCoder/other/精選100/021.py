
N = int(input())
h_list = []
s_list = []
for _ in range(N):
    h,s = map(int,input().split())
    h_list.append(h)
    s_list.append(s)

def is_possible(h):
    # 高さhまでにすべての風船を割り切ることができるか
    limit_list = []
    for i in range(N):

        if h<h_list[i]: # そもそもhより高い位置からスタートする風船がある場合
            return False 
        else:
            limit_t = (h-h_list[i])/s_list[i] # 高さhまでに風船を割るためのギリギリの時間
            limit_list.append(limit_t)
    limit_list.sort() # limitが短い順にソート
    
    for i in range(N):
        if limit_list[i]<i: # 風船を割る時間(i)がlimit時間より長い場合
            return False 
        else:
            continue
    return True

low = 0
high = 1000100010001000

while low+1<high:
    mid = round((low+high)/2)
    if is_possible(mid) ==True: # 高さmidまでに割り切ることができる midを下げる
        high = mid
    else:
        low = mid
print(high)
