m = int(input())
m_list = []
for _ in range(m):
    m_list.append(list(map(int,input().split())))

n = int(input())
n_list = []
for _ in range(n):
    n_list.append(list(map(int,input().split())))

cand_list = []
for i in range(n):
    cand_list.append([n_list[i][0]-m_list[0][0],n_list[i][1]-m_list[0][1]])

for i in range(1,m):
    cand_tmp = []
    for cand in cand_list:
        x = m_list[i][0] + cand[0]
        y = m_list[i][1] + cand[1]
        if [x,y] in n_list: # 二分探索もしくはハッシュテーブルにすることにより高速化可能
            cand_tmp.append(cand)
    cand_list = cand_tmp

print(str(cand_list[0][0])+" "+str(cand_list[0][1]))        
