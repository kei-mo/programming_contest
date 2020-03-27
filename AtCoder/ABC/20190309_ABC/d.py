# A, B = map(int,input().split())

A=2
B=4
binB_len = len(str(bin(B)[2:]))
diff = B-A
s = ''
for i in range(0,binB_len):
    num = B//(2**i) - A//(2**i)
    if num % 2 ==0:
        s = s + str(0)
    else:
        s = s + str(1)

s_int = int(s,10)
ans = diff^s_int
print(ans)