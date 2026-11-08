a, b = map(int,input().split())
khu_dat = a * b
khu_choi = 3.14 * (a / 2) ** 2
trong_cay = khu_dat - khu_choi
print("%.2f" % trong_cay)
