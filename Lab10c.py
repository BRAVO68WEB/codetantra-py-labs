def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    lcm = (x * y) // gcd(x, y)
    return lcm


x = int(input("Enter an integer value: "))
y = int(input("Enter an integer value: "))
print("GCD of {} and {} is".format(x, y), gcd(x, y))
print("LCM of {} and {} is".format(x, y), lcm(x, y))
