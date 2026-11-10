from math import sqrt
a , b , c = map(int, input().split())
if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    print('Day la 3 canh cua mot tam giac')
    cv = a + b + c
    p = cv / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    print("%.2f %.1f" % (cv, s))
else:
    print('Day khong phai la 3 canh cua mot tam giac')