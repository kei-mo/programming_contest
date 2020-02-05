import re
S  = input()
n = len(S)

ans = 0
for i in range(2**n):
    p = bin(i)[2:].zfill(n)
    if p[-1]=="0":
        p = p[:-1]+"1"
    block = re.findall(".*?1",p)
    j = 0
    for b in block:
        ans += int(S[j:j+len(b)])
        j+=len(b)


print(ans)
