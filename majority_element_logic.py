def majority_element_naive(elements):
    element_counts = {}
    for e in elements:
        if e in element_counts:
            element_counts[e] = element_counts[e] + 1
        else:
            element_counts[e] = 1
    for e in element_counts:
        print(element_counts[e])
        if element_counts[e] > (len(elements)/2):
            return 1

    return 0

if __name__ == "__main__":
    print(majority_element_naive([2,3,9,2,2]))