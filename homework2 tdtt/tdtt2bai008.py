from math import sqrt
a, b ,c = map(int, input().split())
p = (a + b + c) / 2
s = sqrt(p * (p - a) * (p - b) * (p - c))
print("%.3f" % (a * b * c / 4 / s))