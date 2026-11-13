TBHK1, TBHK2 = map(float, input().split())
TBCN = ((TBHK1 + 2 * TBHK2) / 3)
print("%.1f" % TBCN)
if TBCN >= 8:
    print('Gioi')
elif TBCN >= 6.5:
    print('Kha')
elif TBCN >= 5.0:
    print('Trung binh')
elif TBCN >= 3.5:
    print('Yeu')
else:
    print('Kem')