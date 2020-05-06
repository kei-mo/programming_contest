"""
方針
各桁ごとに出てくる文字の頻度を並べry
"""
from collections import Counter

def solve():

    top_digit = []
    digits_set = set()
    for i in range(10000):
        q , r = input().split()
        top_digit.append(r[0])
        digits_set.add(r[-1])
    
    top_digit_cnt = Counter(top_digit)
    for c in digits_set:
        if not c in top_digit_cnt:
            ans = c
    char_cnt_sorted = sorted(top_digit_cnt.items(), key=lambda x:x[1],reverse=True)
    for i in range(9):
        ans += char_cnt_sorted[i][0]
    return ans




T = int(input())

for n in range(1,T+1):
    U = int(input())
    ans = solve()
    print('Case #'+str(n)+': '+ans)

