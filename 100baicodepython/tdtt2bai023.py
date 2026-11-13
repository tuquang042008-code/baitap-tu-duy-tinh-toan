n = int(input())
if n < 3:
    print('-')
else:
    for i in range(3, n + 1, 3):
        print(i, end = (' '))