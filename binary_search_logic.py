def binary_search(keys, query):
    right = len(keys)
    left = 0
    foundMatchingElement = -1
    while right > left:
        middleLength = (left + right) // 2
        middle = keys[middleLength]
        print(middleLength)
        if middle == query:
            foundMatchingElement = middleLength
            print(foundMatchingElement)
            right = middleLength
        elif query < middle:
            right = middleLength
        else:
            left = middleLength + 1
    if foundMatchingElement != -1:
        return foundMatchingElement
    return -1

if __name__ == '__main__':
    print(binary_search([1, 1, 1, 4, 4, 4, 5, 5, 5, 7, 7, 7, 9, 9, 9, 13, 13, 13, 16, 16, 16, 20, 20, 20, 35, 35, 35, 57, 67], 5))