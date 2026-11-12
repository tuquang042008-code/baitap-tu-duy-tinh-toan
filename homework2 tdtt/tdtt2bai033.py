from math import sqrt
m , n = map(int, input().split())
dem = 0
def prime(m, n):
    for i in range(m, n + 1):
        if i < 2: dem += 1
        for j in range(2, )