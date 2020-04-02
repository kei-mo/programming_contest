# Alien Rhyme
# Status: AC

import numpy as np
from collections import Counter

def solve():
    n = int(input())
    word_mat = np.full((n,50),"0",dtype=str)
    uniq_member_dict = {}

    max_len  = 0
    for i in range(n):
        w = list(input())
        w_size = len(w)
        word_mat[i,50-w_size:] = np.array(w)
        if w_size>max_len:
            max_len = w_size
    
    group_dict_list = [{} for _ in range(max_len)] # 後ろからi文字目までにどのグループ(メンバー2以上)に属するか {"A":[2,3,4]}
    for i in range(max_len):
        if i==0: # last letter
            l = ""
            member = [x for x in range(n)]
            counter = Counter(word_mat[member,-(i+1)])
            for k,v in counter.items():
                if v>=2:
                    group_dict_list[i][k+l] = [x for x in member if word_mat[x,-(i+1)]==k]
                    uniq_member_dict[k+l] = v
        else:
            for l,member in group_dict_list[i-1].items():
                # get the group devide by previous letter
                #l: letter
                #member: row num which consist this group
                counter = Counter(word_mat[member,-(i+1)])
                for k,v in counter.items():
                    if v>=2: # make new group
                        group_dict_list[i][k+l] = [x for x in member if word_mat[x,-(i+1)]==k] 
                        uniq_member_dict[k+l] = v
                        # uniq_member_dict[l] -= (v//2)*2
                        uniq_member_dict[l] -= v

    num = 0
    # 長い文字列からみていく
    uniq_nm_list = list(uniq_member_dict.keys())
    uniq_nm_len_list = [-1*len(x) for x in uniq_nm_list]
    uniq_nm_sorted = np.argsort(uniq_nm_len_list)

    for p in uniq_nm_sorted:
        k = uniq_nm_list[p]
        v = uniq_member_dict[k]
        if v>=2:
            num+=2
            if len(k)>1:
                uniq_member_dict[k[1:]] += v - 2
        else:
            if len(k)>1:
                uniq_member_dict[k[1:]] += v
    return num


T = int(input())
for t in range(1,T+1):
    ans = solve()
    print("Case #{}: {}".format(t,ans))