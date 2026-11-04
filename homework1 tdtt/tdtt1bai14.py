n = input()
if 'a' <= n <= 'z' or 'A' <= n <= 'Z':
  print(f"{n} la chu cai")
elif '0' <= n <= '9':
  print(f"{n} la chu so")
else:
  print("Khong phai chu cai cung khong phai chu so")