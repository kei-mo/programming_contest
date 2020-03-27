S= input()
max_len = 0
l = 0
# flag = 0 # 前の文字がATGCのいづれか
for i in range(len(S)):
    s = S[i]
    if s == 'A' or s == 'T'  or s == 'G' or s == 'C' :
        l += 1
        if l > max_len:
            max_len = l
    else:
        l = 0
print(max_len)