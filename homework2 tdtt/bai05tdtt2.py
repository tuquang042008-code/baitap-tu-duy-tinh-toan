from math import*
a, b, c = map(float, input().split())
delta = b ** 2 - 4 * a * c
if delta < 0:
    print('Vo nghiem')
elif delta == 0:
    print(-b / 2 * a)
else:
    print((-b + sqrt(delta)) / (2 * a), (-b - sqrt(delta)) / (2 * a))