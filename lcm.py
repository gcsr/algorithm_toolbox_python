
def gcd(a, b):
    if a == 0:
        return b
    if a > b:
        return gcd(b, a)
    else:
        return gcd(b%a, a)

def lcm(a, b):
    gc_gcd = gcd(a, b)
    if gc_gcd == 1:
        return a*b
    else:
        return gc_gcd * lcm(a//gc_gcd, b//gc_gcd)
    # assert False

# 832564823476
if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

