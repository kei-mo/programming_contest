S = input()

a=0
b=0
for i,s in enumerate(S):
    if  i% 2 == 0:
        if s =="0":
            a += 1
        else:
            b += 1
    else:
        if s=="0":
            b+=1
        else:
            a+=1
ans = min(a,b)
print(ans)