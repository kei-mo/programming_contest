from math import log,pow

P = float(input())

def df(x):
    return 1-2*P*log(2)*(pow(2,-2*x/3))/3

def f(x):
    return x + P*(pow(2,-2*x/3))

low = 0
high = 100000

# x=0での微分が正の場合最初からスタートするとよいP年かかる
if df(low)>0:
    print(P)
    exit()
while True:
    middle = (low+high)/2
    if abs(df(middle))<pow(10,-4):
        print(f(middle))
        exit()
    if df(middle)<0:
        low = middle
    else:
        high = middle


