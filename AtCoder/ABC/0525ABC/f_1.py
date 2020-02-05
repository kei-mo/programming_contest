from bisect import insort_left

Q = int(input())
a_list = []
ans1 = 0
length = 0
ans0 = 0
ans0_pos = 0
left_sum =0
right_sum=0
for _ in range(Q):
    input_list = list(map(int,input().split()))
    if input_list[0]==1:
        a = input_list[1]
        insort_left(a_list,a)
        ans1 += input_list[2]
        length += 1

        if length%2==0:
            if a>=ans0:
                ans0_pos += 1
                ans0 = a_list[ans0_pos]
                ans1 += a - ans0

            else:
                ans0_pos += 1
                ans0 = ans0
                ans1 += -1*a + ans0

                
        else:
            if a>=ans0:
                ans0=ans0
                ans0_pos = ans0_pos
                ans1+= a - ans0

            else:
                ans0_pos -= 2
                ans0 = a_list[ans0_pos]
                ans1 += -1*a + a_list[ans0_pos+1]


    else:
        print(str(ans0)+" "+str(ans1))