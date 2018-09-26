def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


print(gcd(8, 12))
print(gcd(5, 12))
print(gcd(24, 12))

print(lcm(2, 4))
print(lcm(3, 4))
print(lcm(30, 4))
