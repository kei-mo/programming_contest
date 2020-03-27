H, A = map(int, input().split())
a = H//A
b = H%A
if b!=0:
    a+=1
print(a)