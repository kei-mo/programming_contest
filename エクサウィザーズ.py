
W = input()
L_set = set(input().split(" "))
W_set = set(W)
ans = 0
for L in L_set:
    if set(L)==W_set:
        ans += 1
print(ans)
