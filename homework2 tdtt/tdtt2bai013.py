a, b , c = map(int, input().split())
if a == b == c:
    print("=")
else:
    print(max(a, b, c))