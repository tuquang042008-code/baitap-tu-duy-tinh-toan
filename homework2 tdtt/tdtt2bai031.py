m, n = map(int, input().split())
if m % 3 == 0:
    m = m
elif m % 3 == 1:
    m = m + 2
else:
    m = m + 1
dem = 0
for i in range(m, n + 1, 3):
    dem += 1
print(dem)