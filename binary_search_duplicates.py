def binary_search(keys, query):
    right = len(keys)
    left = 0
    foundMatchingElement = -1
    while right > left:
        middleLength = (left + right) // 2
        middle = keys[middleLength]
       # print(middleLength)
        if middle == query:
            foundMatchingElement = middleLength
            # print(foundMatchingElement)
            right = middleLength
        elif query < middle:
            right = middleLength
        else:
            left = middleLength + 1
    if foundMatchingElement != -1:
        return foundMatchingElement
    return -1

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
