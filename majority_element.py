def merge_conquer(left, right):
    # print('left', left, "right", right)
    return_array = [None] * (len(left) + len(right))
    l, r , loop_counter= 0, 0, 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            return_array [loop_counter] = left[l]
            loop_counter += 1
            l += 1
        else:
            return_array[loop_counter] = right[r]
            loop_counter += 1
            r += 1
    while l < len(left):
        return_array[loop_counter] = left[l]
        loop_counter += 1
        l += 1
    while r < len(right):
        return_array[loop_counter] = right[r]
        loop_counter += 1
        r += 1

    # print(return_array)
    return return_array

def merge_divide_conquer(ele):
    length = len(ele)
    # print(length)
    if length <= 1:
        return ele
    m = length // 2
    left = merge_divide_conquer(ele[0:m])
    # print(left)
    # print("left", left)
    right = merge_divide_conquer(ele[m:length])
    # print("right", len(right))
    temp = merge_conquer(left, right)
    return temp
def majority_element_naive(elements):
    element_counts = {}
    for e in elements:
        if e in element_counts:
            element_counts[e] = element_counts[e] + 1
        else:
            element_counts[e] = 1
    for e in element_counts:
        if element_counts[e] > (len(elements)/2):
            return 1

    return 0

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))