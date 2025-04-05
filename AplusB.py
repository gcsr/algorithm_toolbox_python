def sum_of_digits(first, second):
    return first+second

if __name__ == '__main__':
    a,b = map(int, input().split())
    print (sum_of_digits(a, b))