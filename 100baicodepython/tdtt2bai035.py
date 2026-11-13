from math import sqrt
m, n = map(int, input().split())
check = 0
sum = 0
def prime(i):
    if i < 2: return False
    for j in range(2, int(sqrt(i)) + 1):
        if i % j == 0: return False
    return True
for i in range(m, n + 1):
    if prime(i):
        sum += i
        check += 1
if check == 0:
    print('-')
else:
    print('%.2f' % (sum / check))

