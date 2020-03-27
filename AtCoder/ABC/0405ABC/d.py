import numpy as np
X,Y,Z,K = map(int,input().split())
A_list = sorted(list(map(int,input().split())),reverse=True)
B_list = sorted(list(map(int,input().split())),reverse=True)
C_list = sorted(list(map(int,input().split())),reverse=True)

tempA,tempB,tempC = 0,0,0
print(A_list[tempA]+B_list[tempB]+C_list[tempC])
temp_list = [A_list[tempA+1] + B_list[tempB]+C_list[tempC],
            A_list[tempA] + B_list[tempB+1]+C_list[tempC],
            A_list[tempA] + B_list[tempB]+C_list[tempC+1]]
for i in range(K-1):
    
    temp_max = np.argmax(temp_list)
    print(temp_list[temp_max])
    if temp_max==0:
        tempA+=1
        if tempA+1<X:
            temp_list[0] = A_list[tempA] + B_list[tempB]+C_list[tempC]
        else:
            temp_list[0] = -1
        temp_list[1] = A_list[tempA-1] + B_list[tempB]+C_list[tempC]
    elif temp_max==1:
        tempB+=1
        if tempB+1<Y:
            temp_list[1] = A_list[tempA] + B_list[tempB+1]+C_list[tempC]
        else:
            temp_list[1] = -1
    else:
        tempC+=1
        if tempC+1<Z:
            temp_list[2] = A_list[tempA] + B_list[tempB]+C_list[tempC+1]
        else:
            temp_list[2] = -1
    

    
