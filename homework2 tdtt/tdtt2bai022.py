n = int(input())
if n <= 50:
    cost = n * 600
elif n <= 100:
    cost = 600 * 50 + 800 * (n - 50)
elif n <= 200:
    cost = 600 * 50 + 800 * 50 + (n - 100) * 1100
else:
    cost = 600 * 50 + 800 * 50 + 100 * 1100 + (n - 200) * 1500
print(cost)