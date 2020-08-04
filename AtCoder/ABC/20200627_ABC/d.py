N = int(input())

def g(x):
    return int(0.5 * x * (x+1))

ans = 0
for i in range(1,N+1):
    ans += i * g(N//i)

print(ans)
