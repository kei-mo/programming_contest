
N,K = map(int,input().split())
a_list = list(map(int,input().split()))

# 建物iをミられる高さにするかいなかのbit探索

ans = 100010001000100010001000

for byte in range(pow(2,N-1)):
    height = a_list[0]
    cost = 0
    if bin(byte).count("1")>=K-1:
        for i in range(N-1):
            if not (byte & 1<<i)==0: # i番目を見る場合
                cost += max(0, height + 1 - a_list[i+1])
                height = max(height + 1, a_list[i+1])
            else:
                height = max(height,a_list[i+1])
        ans = min(ans,cost)
print(ans)