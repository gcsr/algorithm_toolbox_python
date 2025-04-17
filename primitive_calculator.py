def get_last_primitive_op_number(number, min_ops_result_array):
    previous_num = min_ops_result_array[number]
    smaller_index_op = min_ops_result_array[number]
    previous_op_number = number

    if number % 3 == 0:
        if smaller_index_op > min_ops_result_array[number // 3]:
            smaller_index_op =  min_ops_result_array[number // 3]
            previous_op_number = number // 3
    if number % 2 == 0:
        if smaller_index_op > min_ops_result_array[number // 2]:
            smaller_index_op = min_ops_result_array[number // 2]
            previous_op_number = number // 2
    if smaller_index_op > min_ops_result_array[number -1]:
        maller_index_op = min_ops_result_array[number - 1]
        previous_op_number = number -1
    return previous_op_number

def compute_operations(n):
    match n:
        case 0:
            return [0]
        case 1:
            return [1]
        case 2:
            return [1, 2]
        case 3:
            return [1, 3]
    ops_array = []
    ops_array_length = 0
    min_ops_result_array = [x for x in range(n + 1)]
    min_ops_result_array[2] = 1
    min_ops_result_array[3] = 1

    for op_looper in range(4, n + 1):
        if op_looper % 3 == 0:
            # num_coins = money_change_dynamic(min_coins_result_array, money_looper - coin_looper, coins) + 1
            num_ops = min_ops_result_array[op_looper // 3] + 1
            if num_ops < min_ops_result_array[op_looper]:
                min_ops_result_array[op_looper] = num_ops
        if op_looper % 2 == 0:
            # num_coins = money_change_dynamic(min_coins_result_array, money_looper - coin_looper, coins) + 1
            num_ops = min_ops_result_array[op_looper // 2] + 1
            if num_ops < min_ops_result_array[op_looper]:
                min_ops_result_array[op_looper] = num_ops
        num_ops = min_ops_result_array[op_looper - 1] + 1
        if num_ops < min_ops_result_array[op_looper]:
            min_ops_result_array[op_looper] = num_ops
    ops_array.append(n)
    while n > 3:
        n = get_last_primitive_op_number(n, min_ops_result_array)
        ops_array.insert(0, n)
    ops_array.insert(0, 1)
    '''match n:
        case 1:
            ops_array.insert(0, 1)
        case 2:
            ops_array.insert(0, 2)
        case 3:
            ops_array.insert(0, 3)'''
    return ops_array
if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)