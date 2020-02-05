import fractions
import numpy as np
from functools import reduce

def gcd(*numbers):
    return reduce(fractions.gcd, numbers)


N = int(input())
A_list = list(map(int,input().split()))

temp_max= 0
for i in range(N):
        temp_list = A_list.copy()

        if a % temp_max !=0:
                gcd_temp = gcd(*temp_list)
                if type(gcd_temp)== int:
                        gcd_temp = [gcd_temp] 
                if max(gcd_temp)>temp_max:
                        temp_max = max(gcd_temp)

print(temp_max)