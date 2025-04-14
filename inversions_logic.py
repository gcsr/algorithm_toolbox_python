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

def inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions

if __name__ == '__main__':
    # araray = [2,6,3,8,1,2]
    # print (araray[0:6//2])
    # print(araray[6 // 2 : 6])
    static_counter.inversions = 0
    print(merge_divide_conquer([9, 8, 7, 3, 2, 1]))
    print (static_counter.inversions)
    print(merge_divide_conquer([]))
    static_counter.inversions = 0
    print(merge_divide_conquer([2,3,9,2,9]))
    print(static_counter.inversions)