N, Q = map(int,input().split())
s_list = ["_"] + list(input())+ ["_"]
td_list = [input().split() for _ in range(Q)]

l_pos = 1
r_pos = N

for i in range(Q)[::-1]:
    t = td_list[i][0]
    d = td_list[i][1]
    if d == "L":
        if t == s_list[l_pos]:
            l_pos += 1
        elif t == s_list[r_pos]:
            r_pos += 1
    else:
        if t == s_list[l_pos-1]: 
            l_pos -= 1
        elif t == s_list[r_pos+1]:
            r_pos -= 1

print(max(0,r_pos-l_pos-1))        
