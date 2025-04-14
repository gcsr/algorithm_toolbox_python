def static_counter(num):
    static_counter.inversions += num

def merge_conquer(left, right):
    # print('left', left, "right", right)
    return_array = [None] * (len(left) + len(right))
    l, r , loop_counter= 0, 0, 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            return_array [loop_counter] = left[l]
            loop_counter += 1
            l += 1
        else:
            return_array[loop_counter] = right[r]
            loop_counter += 1
            static_counter(1)
            # print(left, right, left[l], right[r], "static", static_counter.inversions)
            r += 1
    if l < len(left):
        static_counter((len(right)) * (len(left) - l - 1))
        # print(left, right, "static left", static_counter.inversions)

    while l < len(left):
        return_array[loop_counter] = left[l]
        loop_counter += 1
        l += 1
    while r < len(right):
        return_array[loop_counter] = right[r]
        loop_counter += 1
        # static_counter()
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

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    static_counter.inversions = 0
    merge_divide_conquer(elements)
    print(static_counter.inversions)