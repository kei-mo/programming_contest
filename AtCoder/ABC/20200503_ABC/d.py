x = int(input())
def ans(x):
    for a in range(0, 1000)[::-1]:
        for b in range(-1000, 1000)[::-1]:
            if a**5 - b**5 == x:
                return a, b
a,b = ans(x)
print(a,b)