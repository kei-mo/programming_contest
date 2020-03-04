S = input()

p = ['A','G','C','T']
flag = 1
num = 0
max_len = 0

for s in S:
    if s in p:
        num+=1
        if num>max_len:
            max_len= num
    else:
        flag =0
        num = 0
print(max_len)