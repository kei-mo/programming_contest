import numpy as np
N,M = map(int,input().split())
AB_list = np.array([list(map(int,input().split())) for _ in range(N)])

cheapStore = np.argsort(AB_list[:,0])
ans = 0
need = M
store = 0
while need > 0:
    store_num = cheapStore[store]
    drink_num = AB_list[store_num][1]
    drink_cost = AB_list[store_num][0]
    if need>=drink_num:
        ans += drink_num * drink_cost
        need -= drink_num
    else:
        ans += need * drink_cost
        need = 0
    store += 1
        
print(ans)
     