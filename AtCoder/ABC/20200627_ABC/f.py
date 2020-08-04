N = int(input())
a_list = list(map(int,input().split()))

xor = 0
if N>= 3:
    for a in a_list[2:]:
        xor ^= a

a = bin(a_list[0])[2:].zfill(100)
b = bin(a_list[1])[2:].zfill(100)
c = bin(xor)[2:].zfill(100)



a_true = ""

x = ""
for i in range(100):
    ai,bi,ci = a[i], b[i], c[i]
    if x!="":
        

    if ai==bi:
        if ci==1:
            ans = '-1'
            break
        else:
            a_true += str(ai)
    elif (ai==1 and bi==0):
        if ci==0:
            x+= "1"
            a_true += str(bi)
        else:
            a_true += str(ai)
    elif (ai==0 and bi==1):
        if ci ==0:

            



    elif (a==0 and b==1):