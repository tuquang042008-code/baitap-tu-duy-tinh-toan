m , n = map(int, input().split())
dem1, dem2 = 0, 0
for i in range(m, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        dem1 += 1
    if i % 2 == 0:
        dem2 += i
print(dem1, dem2)