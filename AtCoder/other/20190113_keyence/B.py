S=input()
answer = 'NO'

if 'keyence' in S:
    answer = 'YES'
elif S[:6] == 'keyenc':
    if S[-1:] == 'e':
        answer = 'YES'
elif S[:5] == 'keyen':
    if S[-2:] == 'ce':
        answer = 'YES'
elif S[:4] == 'keye':
    if S[-3:] == 'nce':
        answer = 'YES'
elif S[:3] == 'key':
    if S[-4:] == 'ence':
        answer = 'YES'
elif S[:2] == 'ke':
    if S[-5:] == 'yence':
        answer = 'YES'
elif S[:1] == 'k':
    if S[-6:] == 'eyence':
        answer = 'YES'

print(answer)