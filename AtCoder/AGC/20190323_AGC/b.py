N = int(input())
ans_list = []
# p_list = list(range(1,N+1))
if N%2 ==0:
    M = int(N*(N-2)/2)
    for i in range(1,N+1):
        pair = N+1-i
        for j in range(i+1,N+1):
            if j != pair:
                ans_list.append([i,j])
#         add_list = [[i,j] for j in range(i+1,N+1) if j != pair]
#         ans_list.extend(add_list)
else:
    M = int((N-1)*(N-1)/2)
    for i in range(1,N):
        pair = N-i
        for j in range(i+1,N):
            if j != pair:
                ans_list.append([i,j])
        ans_list.append([i,N])
        
print(M)
for ans in ans_list:
    print(ans[0],ans[1])

# print(ans_list)