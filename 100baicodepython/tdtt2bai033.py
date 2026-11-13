from math import sqrt
m , n = map(int, input().split())
dem = 0
def check(i):
    if i < 2:
        return False
    for j in range(2, int(sqrt(i)) + 1):
        if i % j == 0:
            return False
    return True
for i in range(m, n + 1):
    if check(i):
        dem += 1
print(dem)