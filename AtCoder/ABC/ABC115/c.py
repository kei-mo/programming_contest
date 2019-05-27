N,K = map(int, input().split())
h_list = [int(input()) for _ in range(N)]
h_list.sort()
diff_list = []
for i in range(N-K+1):
    diff_list.append(h_list[i+K-1] - h_list[i])

print(min(diff_list))
