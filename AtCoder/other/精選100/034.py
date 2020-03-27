# フィボナッチ Fib
N = int(input())

fib_hist = {0:1,1:1}

def Fib(n):
    if (n ==0 or n==1):
        return fib_hist[n]
    else:
        if n-1 in fib_hist:
            b = fib_hist[n-1]
        else:
            b = Fib(n-1)
        
        if n-2 in fib_hist:
            c = fib_hist[n-2]
        else:
            c = Fib(n-2)
        a = b + c
        fib_hist[n] = a
        return a 

 

print(Fib(N))

