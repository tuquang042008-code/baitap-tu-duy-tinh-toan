from math import sqrt
a, b, c = map(int, input().split())
cv = a + b + c
p = cv / 2
s = sqrt(p * (p - a) * (p - b) * (p - c))
print("%.1f %.3f" % (cv, s))