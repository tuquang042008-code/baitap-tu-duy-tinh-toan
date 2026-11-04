from math import *
a, b, c = map(float, input().split())
if a > 0 and b > 0 and c > 0 and a + b > c and b + c > a and a + c > b:
  p = (a + b + c) / 2
  S = sqrt(p * (p - a) * (p - b) * (p - c))
  print('%.1f' % S)
else:
  print('Khong phai 3 canh cua tam giac')
