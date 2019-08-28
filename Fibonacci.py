def F(n):
    a, b = 1, 0
    for i in range(n - 1):
        a, b = a + b, a
    return a

N = int(input())
print(F(N))