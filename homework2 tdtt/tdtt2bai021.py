n = int(input())
if n <= 1:
    cost = 12000 * 1
elif n <= 30:
    cost = 12000 + (n - 1) * 10000
else:
    cost = 12000 + 29 * 10000 + (n - 30) * 9000
print(cost)