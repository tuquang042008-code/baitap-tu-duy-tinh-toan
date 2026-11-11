m, y = map(int, input().split())
if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
    if m == 2:
        print(29)
    elif m == 4 or m == 6 or m == 9 or m == 11:
        print(30)
    else:
        print(31)
else:
    if m == 2:
            print(28)
    elif m == 4 or m == 6 or m == 9 or m == 11:
            print(30)
    else:
            print(31)