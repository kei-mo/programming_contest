S = input()

s0 = S[:len(S)//2]
s1 = S[len(S)//2+1:]

def f(s):
    n = len(s)
    halfn = n//2
    result = True
    for i in range(halfn):
        if s[i] != s[-(i+1)]:
            result = False

    return result

ans = 'Yes'
if not f(S):
    ans = 'No'
elif not f(s0):
    ans = 'No'
elif not f(s1):
    ans = 'No'
print(ans)



