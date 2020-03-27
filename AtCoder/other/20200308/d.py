import numpy as np
N,T= map(int,input().split())
a_list = []
b_list = []
for _ in range(N):
    a,b = map(int,input().split())
    a_list.append(a)
    b_list.append(b)

a_list = np.array(a_list)
b_list = np.array(b_list)

t=1
ans = 0
while True:
    store = np.argmin(a_list*t+b_list)
    end_time = t + a_list[store]*t+b_list[store]

    if end_time<T+0.5: #買い物が時間までに終わる
        ans+=1
        a_list = np.delete(a_list,store)
        b_list = np.delete(b_list,store)
        t = end_time+1
        if len(a_list) == 0: # 全店訪れた
            print(ans)
            exit()
    else:
        print(ans)
        exit()