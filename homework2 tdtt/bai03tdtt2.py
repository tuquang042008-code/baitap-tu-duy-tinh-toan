from math import*
a, b, c = map(float, input().split())
C = a + b + c
p = C / 2
S = sqrt(p * (p - a) * (p - b) * (p - c))
if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('Equilateral')
    elif a == b or b == c or a == c:
        print('isosceles')
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print('right')
    else:
        print('scalene')
    print(S, C)
else:
    print('Khong phai tam giac')

    