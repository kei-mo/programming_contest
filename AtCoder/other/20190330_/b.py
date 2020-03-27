N = int(input())
s = input()
b = s.count('B')
r = s.count('R')
if r>b:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)