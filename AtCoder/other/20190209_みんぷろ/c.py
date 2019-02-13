K, A, B = map(int,input().split())
if B-A <=2:
    ans = K + 1
elif K <= A:
    ans = K +1
else:
    # A-1回たたく
    time = K - (A-1)
    ans = A 
    # n回 A枚をBに交換する 2*n回数分の操作
    n = time // 2
    mod = time % 2
    ans += n*(-A + B)
    ans += mod

print(ans)
