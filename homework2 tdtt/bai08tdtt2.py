a, b, c, d, m, n = map(float, input().split())
x = ((n - (d * m / b)) / (c - (a * d / b)))
y = (m - a * x) / b
print(x, y)