N = int(input())
ans = 0
ans = 4**N - 3 - (N-3)*23
print(ans%(10**9+7))
