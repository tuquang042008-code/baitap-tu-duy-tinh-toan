c = input()
if 'a' <= c <= 'z':
    print(chr(ord(c) - 32))
else:
    print(chr(ord(c) + 32))
