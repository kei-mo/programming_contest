H = int(input())
a = H
b = 0
while a>1:
    b+=1
    a = a //2
    
ans = sum([2**x for x in range(b+1)])
print(ans)