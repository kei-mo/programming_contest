A,B = input().split()

sa = 0
sb = 0

for a in A:
    sa += int(a)

for b in B:
    sb += int(b)

if sb>sa:
    print(sb)
else:
    print(sa)