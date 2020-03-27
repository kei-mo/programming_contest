import numpy as np

N=int(input())	
listA = list(map(int,input().split()))

minA = min(listA)

while True:
    minA = min(listA)
    minApos = np.argmin(listA)
    listA = [x % minA for x in listA]
    listA[minApos] = minA
    listA= [x for x in listA if x >0]
    if len(set(listA))==1:
        print(minA)
        break