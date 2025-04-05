def fibonacci_sum(n):
    if n == 0:
        return 0
    previous, current, sum = 0, 1, 1
    for looper in range(2, n+1):
       # sum = 0
       previous, current, sum = current, (previous + current)%10, (sum + previous + current) % 10
    return sum
# 832564823476
# 2147483647
# 100000000000

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
