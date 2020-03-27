import bisect

N= int(input())
a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))
c_list = list(map(int,input().split()))
c_num = len(c_list)

a_list.sort()
c_list.sort()

ans = 0
for b in b_list:
    a_point = bisect.bisect_left(a_list,b)
    c_point = bisect.bisect(c_list,b)
    
    ans+= a_point*(c_num-c_point)
print(ans)
