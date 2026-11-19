a, b, i1, i2, r = map(float, input().split())
if (a - i1) ** 2 + (b - i2) ** 2 == r ** 2:
    print('Thuoc duong tron')
else:
    print('Khong thuoc duong tron')