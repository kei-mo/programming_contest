import numpy as np
H, W = map(int,input().split())

matrix = []
for i in range(H):
    matrix.append(list(input()))
matrix = np.array(matrix)
black_list = np.where(matrix=='#')
count = 0
queue = []

for i in range(len(black_list[0])):
    queue.append([black_list[0][i], black_list[1][i]])


def search(x,y,matrix):
    q = []
    # 上を見る       
    if not x == 0:
        state = matrix[x-1,y]
        if state == ".":
            q.append([x-1,y])
            matrix[x-1,y] = "#"

    # 下を見る       
    if not x == H-1:
        
        state = matrix[x+1,y]
        if state ==".":
            q.append([x+1,y])
            matrix[x+1,y] = "#"

    # 左を見る       
    if not y == 0:
        state = matrix[x,y-1]
        if state == ".":
            q.append([x,y-1])
            matrix[x,y-1] = "#" 
        
    # 右を見る       
    if not y == W-1:
        state = matrix[x,y+1]
        if state == ".":
            q.append([x,y+1])
            matrix[x,y+1] = "#"
    
    return matrix, q


while True:
    count +=1
    next_queue = []
    for pos in queue:
        matrix,q = search(pos[0],pos[1],matrix)
        if len(q)!=0:
            next_queue.extend(q)
    queue = next_queue

    white_list = np.where(matrix=='.')
    white_num = len(white_list[0])
    if white_num==0:
        break

print(count)

