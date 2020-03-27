import numpy as np 
M,N = map(int,input().split())
K= int(input())

planet_matrix = [["X" for _ in range(N+1)]]
for _ in range(M):
    planet_matrix.append(list("X"+input()))
planet_matrix = np.array(planet_matrix)
j_num = (planet_matrix=='J').cumsum(axis=0).cumsum(axis=1)
o_num = (planet_matrix=='O').cumsum(axis=0).cumsum(axis=1)
# i_num = (planet_matrix=='I').cumsum(axis=0).cumsum(axis=1)


# (0,0)から(i,j)を頂点とする長方形に含まれる累積和
# j_num = np.zeros((M+1,N+1)) # [[0 for _ in range(N+1)] for _ in range(M+1)]
# o_num = np.zeros((M+1,N+1)) # [[0 for _ in range(N+1)] for _ in range(M+1)]
# i_num = np.zeros((M+1,N+1)) # [[0 for _ in range(N+1)] for _ in range(M+1)]
# j_num = np.array(j_num)
# o_num = np.array(o_num)
# i_num = np.array(i_num)

# for i in range(1,M+1):
#     for j in range(1,N+1):
#         j_num[i][j] = j_num[i][j-1] + j_num[i-1][j] - j_num[i-1][j-1]
#         o_num[i][j] = o_num[i][j-1] + o_num[i-1][j] - o_num[i-1][j-1]
#         i_num[i][j] = i_num[i][j-1] + i_num[i-1][j] - i_num[i-1][j-1]

#         land_type = planet_matrix[i-1][j-1]
#         if land_type=='J':
#             j_num[i][j] +=1
#         if land_type=='O':
#             o_num[i][j] +=1
#         if land_type=='I':
#             i_num[i][j] +=1

for i in range(K):
    a,b,c,d = map(int,input().split())
    
    j = j_num[c][d] - j_num[c][b-1] - j_num[a-1][d] + j_num[a-1][b-1]
    o = o_num[c][d] - o_num[c][b-1] - o_num[a-1][d] + o_num[a-1][b-1]
    i=(c-a+1)*(d-b+1) - j - o
    # i = i_num[c][d] - i_num[c][b-1] - i_num[a-1][d] + i_num[a-1][b-1]
    print(str(int(j))+" "+str(int(o)) + " "+ str(int(i)))

            

