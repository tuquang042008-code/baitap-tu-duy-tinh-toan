m, n = map(int, input().split())
def gcd(m, n):
    while n != 0:
        du = m % n
        m = n
        n = du
    return m
print(gcd(m, n)) 