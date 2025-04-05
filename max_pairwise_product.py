def findMaxNotEquals(numbers, highest):
    secondMax = -1
    counter = 0
    for x in numbers:
        if (x == highest):
            counter += 1
        if (x != highest and x > secondMax):
            secondMax = x
    return highest if counter > 1 else secondMax

def find_first_second_largest_numbers(numbers):
    biggest = max(numbers);
    secondBiggest = findMaxNotEquals(numbers, biggest);
    return [biggest, secondBiggest]

def max_pairwise_product(numbers):
    first_two_elements = find_first_second_largest_numbers(numbers)
    return first_two_elements[1] * first_two_elements[0]


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
