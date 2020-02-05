from bisect import insort_left

Q = int(input())
a_list = []
scalar = 0
length = 0
for _ in range(Q):
    input_list = list(map(int,input().split()))
    if input_list[0]==1:
        a = input_list[1]
        insort_left(a_list,a)
        scalar += input_list[2]
        length += 1
    else:
        # unique_a_list =list(set(a_list.copy())) 
        if length%2==0:
            ans0_pos =int(length/2 - 1)
            ans0 = a_list[ans0_pos]
            ans1 = -1* sum(a_list[:ans0_pos+1]) + sum(a_list[ans0_pos+1:])+scalar

        else:
            ans0_pos = int(length/2-0.5)
            
            ans0 = a_list[ans0_pos]
            ans1 = -1* sum(a_list[:ans0_pos]) + sum(a_list[ans0_pos+1:]) + scalar
        print(str(ans0)+" "+str(ans1))