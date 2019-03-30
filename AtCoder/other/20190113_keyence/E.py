import numpy
N = 3
D = 1
listA = [1,100,1]
order = sorted(listA)
cost = (N-1) * D + 2 * sum(listA) - listA[0] -listA[-1]
precost = inf

while 1:
    biggest = order.pop()
    