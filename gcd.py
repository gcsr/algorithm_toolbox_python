def gcd(a, b):
    if a == 0:
        return b
    if a > b:
        return gcd(b, a)
    else:
        return gcd(b%a, a)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
