S= input()
Q = int(input())
rev_cnt = 0

a = "0"
a_rev_cnt = 0
b = "0"
b_rev_cnt = 0

for _ in range(Q):
    query = input()
    if query[0]=="1":
        t = 1
        rev_cnt  = -1*rev_cnt+1
        a,b = b,a

    else:
        t,f,c = query.split()
        if f=="1":
            if rev_cnt ==0:
                a = c+a
            else:
                a = a+c

        elif f=="2":
            if rev_cnt ==0:
                b = b+c
            else:
                b = c+b
if a[0]=="0":
    a = a[::-1]
a = a[:-1]
if b[-1]=="0":
    b = b[::-1]
b = b[1:]


if rev_cnt%2==0:
    ans = a+S+b
else:
    ans = a+S[::-1]+b
print(ans)