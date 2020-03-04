from collections import Counter
N = int(input())
a_dict = Counter(map(int,input().split()))

if a_dict.most_common()[0][1]>1:
    ans = "NO"
else:
    ans = "YES"
print(ans)