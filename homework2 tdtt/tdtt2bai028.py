from math import sqrt
n = int(input())
dem = 0
for i in range(1, int(sqrt(n)) + 1):
    if n % i == 0:
        dem += 1
        if n % i != i:
            dem += 1
print(dem)