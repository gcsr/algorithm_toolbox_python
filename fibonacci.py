def fibonacci_number(n):
    if n == 0:
        return 0
    fibonacci_numbers = [None]*(n+1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for looper in range(2, n+1):
        fibonacci_numbers[looper] = fibonacci_numbers[looper-1] + fibonacci_numbers[looper-2]
    return fibonacci_numbers[n]


if __name__ == '__main__':
    # input_n = int(input())
    for i in range(20):
        print(fibonacci_number(i))
