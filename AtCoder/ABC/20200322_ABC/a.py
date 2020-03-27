N,M = map(int,input().split())

ans = 0
if N>=2:
    ans+=N*(N-1)/2

if M>=2:
    ans+=M*(M-1)/2

print(int(ans))