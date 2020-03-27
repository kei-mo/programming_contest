N = int(input())
As = list(map(int, input().split()))
dic = {}
for A in As:
    if A in dic.keys():
        dic[A] += 1
    else:
        dic[A] = 1
total = 0
for A in dic.keys():
    a = dic[A]
    if a > 1:
        temp = a*(a-1)/2
        total += temp
for i in range(N):
    Ai = As[i]
    if dic[Ai] == 2:
        print(int(total-1))
    elif dic[Ai] > 2:
        a = dic[Ai]
        diff = (a*(a-1) - (a-1)*(a-2))/2
        print(int(total - diff)) 
    else:
        print(int(total))