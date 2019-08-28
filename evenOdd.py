
from math import  sqrt

n = int(input())

s = round(sqrt(n))

if s**2 == n:

    print("odd")

else:

    print("even")