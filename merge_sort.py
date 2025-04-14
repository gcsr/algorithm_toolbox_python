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

def merge_divide(ele):
    length = len(ele)
    # print(length)
    if length <= 1:
        return ele
    m = length // 2
    left = merge_divide(ele[0:m])
    # print(left)
    # print("left", left)
    right = merge_divide(ele[m:length])
    # print("right", len(right))
    temp = merge_conquer(left, right)
    return temp

if __name__ == '__main__':
    # araray = [2,6,3,8,1,2]
    # print (araray[0:6//2])
    # print(araray[6 // 2 : 6])
    print(merge_divide([2,6,3,8,1,5,7,9,8,12,34]))
    print(merge_divide([]))