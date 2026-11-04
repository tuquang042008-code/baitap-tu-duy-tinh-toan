name = input("Ten chu ho: ")
lastmonth = int(input("Chi so thang truoc: "))
thismonth = int(input("Chi so thang nay: "))
index = thismonth - lastmonth
if 0 <= index <= 50:
  cost = index * 1984
elif index <= 100:
  cost = 50 * 1984 + (index - 50) * 2050
elif index <= 200:
  cost = 50 * 1984 + 50 * 2050 + (index - 100) * 2380
elif index <= 300:
  cost = 50 * 1984 + 50 * 2050 + 100 * 2380 + (index - 200) * 2998
elif index <= 400:
  cost = 50 * 1984 + 50 * 2050 + 100 * 2380 + 100 * 2998 + (index - 300) * 3350
else:
  cost = 50 * 1984 + 50 * 2050 + 100 * 2380 + 100 * 2998 + 100 * 3350 + (index - 400) * 3460
tong = int(cost * 1.08)
print(f"Ho va ten: {name}")
print(f"Tien phai tra la: {tong}")
