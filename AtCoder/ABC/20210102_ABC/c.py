N = int(input())
set0 = set()
set1 = set() # !

for _ in range(N):
    a = input()
    if a[0] == '!':
        set1.add(a[1:])
    else:
        set0.add(a)

s_intersection = set1 & set0
if len(s_intersection)==0:
    print('satisfiable')
else:
    print(s_intersection.pop())
