def fibonacci_last_digit(n):
    if n == 0:
        return 0
    fibonacci_numbers_last_digit = [None] * (n + 1)
    fibonacci_numbers_last_digit[0] = 0
    fibonacci_numbers_last_digit[1] = 1
    for looper in range(2, n + 1):
        fibonacci_numbers_last_digit[looper] = (fibonacci_numbers_last_digit[looper - 1] + fibonacci_numbers_last_digit[looper - 2]) %10
    return fibonacci_numbers_last_digit[n]


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))