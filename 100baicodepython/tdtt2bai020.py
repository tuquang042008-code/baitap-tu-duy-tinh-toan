n = int(input())
print(n // 5000, end = (' '))
n = n % 5000
print(n // 2000, end = (' '))
n = n % 2000
print(n)