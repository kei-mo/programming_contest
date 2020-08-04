K = int(input())

if (K%2==0 or K%5==0):
    print(-1)
else:
    num = '7'
    flag = False
    for i in range(1000000):
        if int(num) %K ==0:
            print(len(num))
            flag = True
            break
        num += '7'
    if not flag:
        print(-1)
