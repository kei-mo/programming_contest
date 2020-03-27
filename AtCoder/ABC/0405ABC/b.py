inputs = [int(input()) for _ in range(5)]
inputs_mod10 = [i%10 for i in inputs]
ans = 0
min_mod = 10
for i in range(5):
    if inputs_mod10[i]==0:
        ans += inputs[i]
    else:
        ans += (inputs[i]//10 +1 )*10
        min_mod = min(min_mod,inputs_mod10[i])
ans -= (10-min_mod)
print(ans)